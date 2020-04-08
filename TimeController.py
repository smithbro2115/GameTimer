from PyQt5.QtCore import QObject, QThreadPool, QRunnable, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem
import time
from datetime import datetime
from datetime import timedelta
from Users import User, TimedUser, load_users
from Utils.CachingUtils import read_from_cache, write_to_cache
from Utils import UsefulUtils
from configparser import NoOptionError, NoSectionError
from Notifications import NotificationManager


class TimeController:
    def __init__(self, parent):
        self.parent = parent
        self.current_users = {}
        self._current_user = None
        self.current_user = None
        self.last_load = None
        self.load_queued = False
        self.notification_manager = NotificationManager(self)
        self.time_since_last_warning_tone = None
        self.thread_pool = QThreadPool()
        self.time_checker = None
        self.make_time_checker()

    @property
    def current_user(self):
        return self._current_user

    @current_user.setter
    def current_user(self, value):
        self._current_user = value

    def make_time_checker(self):
        try:
            self.time_checker.canceled = True
        except AttributeError:
            pass
        self.time_checker = TimeChecker(self)
        self.parent.connect_time_checker_signals(self.time_checker)
        self.time_checker.signals.warning_time.connect(self.notification_manager.check_warning)
        self.time_checker.signals.times_up.connect(self.notification_manager.check_alarm)
        self.time_checker.signals.updated_remotely.connect(self.parent.updated_remotely)
        self.time_checker.signals.file_not_found.connect(self.load)
        self.thread_pool.start(self.time_checker)

    def reset(self):
        self.switch_user(None)

    def get_last_user(self):
        try:
            self.switch_user(self.current_users[read_from_cache("LAST_USED", "last_user_id")])
        except (NoSectionError, NoOptionError, KeyError):
            pass

    def load(self):
        try:
            self.current_users = self.convert_users_list_to_dict(load_users())
        except FileNotFoundError:
            self.parent.users_folder_could_not_be_found()
            self.make_time_checker()
        else:
            self.last_load = datetime.now()
            self.load_queued = False
            self.load_to_gui()
            if not self.admin_exists():
                self.parent.no_admin()

    def reload(self):
        self.load()
        return self.last_load

    def admin_exists(self):
        for user in self.current_users.values():
            if user.user_type == "admin":
                return True
        return False

    @staticmethod
    def convert_users_list_to_dict(users):
        user_dict = {}
        for user in users:
            user_dict[user.id] = user
        return user_dict

    def load_to_gui(self):
        self.parent.load_users(self.current_users)

    def load_new_current_user_into_gui(self, user):
        self.parent.gui_message_controller.user_switched(user)
        try:
            self.parent.userListWidget.setCurrentItem(self.parent.get_list_item_from_id(user.id))
        except AttributeError:
            pass

    def switch_user(self, user, login_required=True):
        if not login_required or self.parent.log_in(user):
            self.current_user = user
            self.notification_manager.reset()
            self.load_new_current_user_into_gui(self.current_user)
            try:
                if user.user_type != "admin":
                    write_to_cache("LAST_USED", "last_user_id", self.current_user.id)
                else:
                    write_to_cache("LAST_USED", "last_user_id", '')
            except AttributeError:
                write_to_cache("LAST_USED", "last_user_id", '')

    def generate_report(self, user: TimedUser):
        clock_history = user.user_clock.history
        time_limit_history = user.time_limit.history
        for time_limit_date, time_limit in time_limit_history.items():
            yield self.make_day(time_limit_date, time_limit, clock_history)
            i = 1
            while True:
                date = time_limit_date + timedelta(days=i)
                if self.should_bridge_date(date, time_limit_history):
                    i += 1
                    yield self.make_day(date, time_limit, clock_history)
                else:
                    break

    @staticmethod
    def make_day(date, time_limit, clock_history):
        day = {'date': date, 'time_limit': time_limit}
        try:
            time_played = clock_history[date]
        except KeyError:
            time_played = timedelta(seconds=0)
        day["time_played"] = time_played
        day["went_over_by"] = time_limit - time_played
        return day

    @staticmethod
    def should_bridge_date(date, dates):
        return date not in dates.keys() and datetime.now().date() >= date

    def interact(self):
        if self.current_user:
            self.notification_manager.reset()
            self.current_user.user_clock.interact()
            self.notification_manager.interacted(self.current_user)


class TimeCheckerSignals(QObject):
    warning_time = pyqtSignal(User)
    times_up = pyqtSignal(User)
    update_time_left = pyqtSignal(User)
    updated_remotely = pyqtSignal()
    file_not_found = pyqtSignal()


class TimeChecker(QRunnable):
    def __init__(self, parent):
        super(TimeChecker, self).__init__()
        self.signals = TimeCheckerSignals()
        self.parent = parent
        self.canceled = False

    @pyqtSlot()
    def run(self):
        while not self.canceled:
            try:
                self.check_for_remote_update()
                self.run_users_checks()
            except (FileNotFoundError, OSError):
                self.signals.file_not_found.emit()
                break
            except RuntimeError:
                break
            time.sleep(.5)

    def run_users_checks(self):
        try:
            for user in self.parent.current_users.values():
                try:
                    if user.user_type == "timed_user":
                        self.check_for_time_up(user)
                        self.check_for_warning_time(user)
                        self.update_time(user)
                except KeyError:
                    pass
                except FileNotFoundError:
                    pass
        except RuntimeError:
            pass

    def check_for_remote_update(self):
        try:
            if UsefulUtils.read_from_user_edited_notify_file() > self.parent.last_load and not self.parent.load_queued:
                self.signals.updated_remotely.emit()
                raise RuntimeError
        except TypeError:
            pass

    def check_for_time_up(self, user):
        if user.is_time_up():
            self.signals.times_up.emit(user)

    def check_for_warning_time(self, user):
        if user.is_warning_time():
            self.signals.warning_time.emit(user)

    def update_time(self, user):
        if user == self.parent.current_user:
            self.signals.update_time_left.emit(user)
