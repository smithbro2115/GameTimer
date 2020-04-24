from GUI.NewUserUI import Ui_Dialog as NewUserUI
from GUI import AreYouSureDialog as AreYouSureUI, Error as ErrorUI, SettingsUI, LogInUI, AdminUserWidgetUI,\
    TimedUserWidgetUI, ModifyTimeDialogUI, PathNotFoundUI, CrashReportUI
from PyQt5 import QtCore, QtWidgets, QtGui
from Notifications import NotificationManager
from Utils.UsefulUtils import convert_string_to_bool
from Utils.CachingUtils import read_from_config
from Utils.FileUtils import resource_path
import qdarkstyle
from datetime import datetime, timedelta
from Reminders import Reminder
import os


class DialogTemplate(QtWidgets.QDialog):
    def __init__(self, ui, parent=None):
        super(DialogTemplate, self).__init__(parent=parent)
        self.ui = ui()
        self.ui.setupUi(self)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


class LogInDialog(DialogTemplate):
    def __init__(self, user_name, password, parent=None):
        super(LogInDialog, self).__init__(LogInUI.Ui_Dialog, parent=parent)
        self.user_name = user_name
        self.password = password
        self.ui.userLabel.setText(self.user_name)
        self.ui.passwordLineEdit.textChanged.connect(self.verify_password_field)
        self.ui.acceptPushButton.clicked.connect(self.accept)
        self.ui.cancelPushButton.clicked.connect(self.close)
        self.ui.msgLabel.setVisible(False)
        self.verify_password_field()

    def verify_password_field(self):
        field = self.ui.passwordLineEdit
        if field.text() == "":
            self.ui.acceptPushButton.setEnabled(False)
            return False
        self.ui.acceptPushButton.setEnabled(True)

    def accept(self):
        if self.ui.passwordLineEdit.text() != self.password:
            self.ui.msgLabel.setText("Password is Incorrect")
            self.ui.msgLabel.setVisible(True)
        else:
            super(LogInDialog, self).accept()


class NewUserDialog(DialogTemplate):
    def __init__(self, parent=None, **kwargs):
        super(NewUserDialog, self).__init__(NewUserUI, parent)
        self.admin = False
        self.required_fields = {"base_time": self.ui.baseTimeLineEdit, "name": self.ui.nameLineEdit}
        self.timed_user_widgets = [self.ui.baseTimeWidget, self.ui.warningTimeWidget, self.ui.followGlobalWidget]
        self.add_kwargs_to_dialog(kwargs)
        self.set_required_fields()
        self.verify_required_fields()
        self.ui.baseTimeLineEdit.setValidator(QtGui.QIntValidator())
        self.ui.warningTimeLineEdit.setValidator(QtGui.QIntValidator())
        self.ui.acceptPushButton.clicked.connect(self.accept)
        self.ui.cancelPushButton.clicked.connect(self.close)
        self.ui.followGlobalCheckBox.clicked.connect(self.follow_global_changed)
        self.ui.adminCheckBox.clicked.connect(self.admin_changed)

    def set_required_fields(self):
        for field in self.required_fields.values():
            field.textChanged.connect(self.verify_required_fields)

    def verify_required_fields(self):
        for field in self.required_fields.values():
            if field.text().strip() == "":
                self.ui.acceptPushButton.setEnabled(False)
                return False
        self.ui.acceptPushButton.setEnabled(True)

    def follow_global_changed(self):
        if not self.admin:
            base_time_field = self.ui.baseTimeLineEdit
            base_time_label = self.ui.baseLabel
            warning_widget = self.ui.warningTimeWidget
            base_widget = self.ui.baseTimeWidget
            if self.ui.followGlobalCheckBox.isChecked():
                del self.required_fields["base_time"]
                base_time_label.setText("Base Amount of Time in Minutes")
                base_widget.setEnabled(False)
                warning_widget.setEnabled(False)
            else:
                self.required_fields["base_time"] = base_time_field
                base_time_label.setText("*Base Amount of Time in Minutes")
                base_widget.setEnabled(True)
                warning_widget.setEnabled(True)
            self.verify_required_fields()

    def admin_changed(self):
        if self.ui.adminCheckBox.isChecked():
            self.set_admin()
        else:
            self.set_timed_user()

    def set_admin(self):
        for widget in self.timed_user_widgets:
            widget.setVisible(False)
        del self.required_fields['base_time']
        self.verify_required_fields()
        self.admin = True
        self.adjustSize()

    def set_timed_user(self):
        self.setWindowTitle("New User")
        for widget in self.timed_user_widgets:
            widget.setVisible(True)
        self.required_fields['base_time'] = self.ui.baseTimeLineEdit
        self.admin = False
        self.verify_required_fields()
        self.adjustSize()

    def add_kwargs_to_dialog(self, kwargs):
        for key, value in kwargs.items():
            if key == "name":
                self.ui.nameLineEdit.setText(value)
            elif key == "base_time":
                self.ui.baseTimeLineEdit.setText(value[:-1])
            elif key == "warning_time":
                self.ui.warningTimeLineEdit.setText(value)
            elif key == "follow_global":
                self.ui.followGlobalCheckBox.setChecked(convert_string_to_bool(value))
                self.follow_global_changed()
            elif key == "user_type" and value == 'admin':
                self.ui.adminCheckBox.setChecked(True)
                self.set_admin()
            elif key == "admin_only" and value is True:
                self.ui.adminCheckBox.setChecked(True)
                self.ui.adminCheckBox.setEnabled(False)
                self.setWindowTitle("New Admin")
                self.set_admin()
            elif key == "password":
                self.ui.passwordLineEdit.setText(value)
            elif key == 'edit' and value is True:
                self.setWindowTitle("Edit User")


class SettingsDialog(DialogTemplate):
    def __init__(self, parent=None, **kwargs):
        super(SettingsDialog, self).__init__(SettingsUI.Ui_Dialog, parent)
        self.default_users_location = None
        self.ui.usersPathLineEdit.textChanged.connect(self.check_if_valid_accept)
        self.add_kwargs_to_dialog(kwargs)
        self.ui.globalWarningTimeLineEdit.setValidator(QtGui.QIntValidator())
        self.ui.globalTimeLineEdit.setValidator(QtGui.QIntValidator())
        self.ui.usersPathToolButton.clicked.connect(self.users_path_tool_clicked)
        self.ui.acceptPushButton.clicked.connect(self.accept)
        self.ui.cancelPushButton.clicked.connect(self.close)
        self.check_if_valid_accept()

    def validate_fields(self):
        user_path_text = self.ui.usersPathLineEdit.text()
        if user_path_text != "" and os.path.isdir(user_path_text):
            self.default_users_location = user_path_text
            return True
        return False

    def users_path_tool_clicked(self):
        user_path_line_edit = self.ui.usersPathLineEdit
        dialog = GetFolderLocationDialog(self.default_users_location)
        result = dialog.get_folder_path()
        if result != "":
            user_path_line_edit.setText(result)

    def check_if_valid_accept(self):
        self.ui.acceptPushButton.setEnabled(self.validate_fields())

    def add_kwargs_to_dialog(self, kwargs):
        for key, value in kwargs.items():
            if key == "global_time":
                try:
                    self.ui.globalTimeLineEdit.setText(value[:-1])
                except TypeError:
                    self.ui.globalTimeLineEdit.setText("")
            elif key == "global_warning_time":
                self.ui.globalWarningTimeLineEdit.setText(value)
            elif key == "users_path":
                self.ui.usersPathLineEdit.setText(value)


class PathNotFoundDialog(DialogTemplate):
    def __init__(self, parent=None):
        super(PathNotFoundDialog, self).__init__(PathNotFoundUI.Ui_Dialog, parent=parent)
        self.state = ""
        self.ui.closePushButton.clicked.connect(self.close)
        self.ui.descriptionLabel.setText(self.ui.descriptionLabel.text()
                                         .replace("[path]", read_from_config("SETTINGS", "users_path")))
        self.ui.retryPushButton.clicked.connect(self.retry_clicked)
        self.ui.newPathPushButton.clicked.connect(self.new_path_clicked)

    def retry_clicked(self):
        self.state = "retry"
        self.accept()

    def new_path_clicked(self):
        self.state = "new_path"
        self.accept()


class ModifyTimeDialog(DialogTemplate):
    def __init__(self, user, parent=None):
        super(ModifyTimeDialog, self).__init__(ModifyTimeDialogUI.Ui_Dialog, parent=parent)
        self.user = user
        self.ui.timeLineEdit.setValidator(QtGui.QIntValidator())
        self.ui.userLabel.setText(f"Modifying {user.name}'s Time")
        self.time_left = 0
        self.set_time_left_line_edit()
        self.ui.timeSpinBox.valueChanged.connect(self.spin_box_changed)
        self.ui.timeLineEdit.textChanged.connect(self.line_edit_changed)

    def spin_box_changed(self):
        self.set_time_left_line_edit()
        if self.ui.timeSpinBox.value() > 0:
            self.ui.timeSpinBox.setPrefix("+")
        else:
            self.ui.timeSpinBox.setPrefix("")

    def line_edit_changed(self):
        self.set_modify_box()
        if self.ui.timeLineEdit.text() == "":
            self.ui.timeLineEdit.setText(str(0))

    def set_time_left_line_edit(self):
        self.time_left = int(self.user.time_left().total_seconds()/60) + self.ui.timeSpinBox.value()
        self.ui.timeLineEdit.setText(str(self.time_left))

    def set_modify_box(self):
        try:
            changed_by = (int(self.ui.timeLineEdit.text()) - int(self.user.time_left().total_seconds()/60))
            self.ui.timeSpinBox.setValue(changed_by)
        except ValueError:
            changed_by = (0 - int(self.user.time_left().total_seconds() / 60))
            self.ui.timeSpinBox.setValue(changed_by)


class AreYouSureDialog(DialogTemplate):
    def __init__(self, msg, parent=None):
        super(AreYouSureDialog, self).__init__(AreYouSureUI.Ui_Dialog, parent=parent)
        self.ui.msgLabel.setText(msg)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


class GetFolderLocationDialog(QtWidgets.QFileDialog):
    def __init__(self, default_location, caption="Select Folder"):
        super(GetFolderLocationDialog, self).__init__()
        self.default_location = default_location
        self.caption = caption

    def get_folder_path(self):
        result = self.getExistingDirectory(caption=self.caption, directory=self.default_location)
        return result


class ErrorDialog(DialogTemplate):
    def __init__(self, msg, window_label="Error", parent=None):
        super(ErrorDialog, self).__init__(ErrorUI.Ui_Dialog, parent=parent)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.setWindowTitle(window_label)
        self.ui.messageLabel.setWordWrap(True)
        self.ui.messageLabel.setText(msg)


class WidgetTemplate(QtWidgets.QWidget):
    def __init__(self, ui, parent):
        super(WidgetTemplate, self).__init__(parent=parent)
        self.ui = ui()
        self.ui.setupUi(self)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            try:
                return self.ui.__dict__[item]
            except KeyError:
                pass
        return super(WidgetTemplate, self).__getattr__(item)


def reload_last_user_after(function):
    def wrapper(*args, **kwargs):
        try:
            self = args[0]
            last_user_id = self.current_selected_user.id
            result = function(*args, **kwargs)
            if last_user_id:
                try:
                    self.adminUserListWidget.setCurrentItem(self.get_item_by_user_id(last_user_id))
                except AttributeError:
                    pass
            return result
        except AttributeError:
            return function(*args, **kwargs)
    return wrapper


class AdminUserWidget(WidgetTemplate):
    def __init__(self, user, parent_gui, parent=None):
        super(AdminUserWidget, self).__init__(AdminUserWidgetUI.Ui_Form, parent=parent)
        self.parent_gui = parent_gui
        self.ui.newUserPushButton.clicked.connect(self.add_user_pushed)
        self.adminUserListWidget = KeepSelectionWhenInactiveList()
        self.user_buttons = [self.ui.editUserPushButton, self.ui.deleteUserPushButton]
        self.timed_user_buttons = [self.ui.modifyTimePushButton, self.ui.userReportPushButton] + self.user_buttons
        self.ui.userSelectionWidget.layout().addWidget(self.adminUserListWidget, 0, 0)
        self.ui.editUserPushButton.clicked.connect(self.edit_user_pushed)
        self.ui.deleteUserPushButton.clicked.connect(self.delete_user_pushed)
        self.ui.modifyTimePushButton.clicked.connect(self.modify_time_pushed)
        self.ui.userReportPushButton.clicked.connect(self.report_push_button_clicked)
        self.ui.reportTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.adminUserListWidget.sortItems(QtCore.Qt.AscendingOrder)
        self.ui.reportTableWidget.verticalHeader().setVisible(False)
        self.ui.reportTableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui.userReportPushButton.setVisible(False)
        self.adminUserListWidget.itemSelectionChanged.connect(self.admin_list_selection_changed)
        self.ui.refreshPushButton.clicked.connect(self.refresh_clicked)
        self.set_user_options()
        self.set_user_label(user)
        self.add_users()

    @property
    def current_selected_user(self):
        try:
            return self.adminUserListWidget.currentItem().data(8)
        except AttributeError:
            return None

    def admin_list_selection_changed(self):
        self.ui.reportTableWidget.setRowCount(0)
        self.set_user_options()
        try:
            self.report_push_button_clicked()
        except AttributeError:
            pass
        except FileNotFoundError:
            pass

    def set_user_options(self):
        self.enable_disable_list(self.timed_user_buttons, False)
        try:
            if self.current_selected_user.user_type == "admin":
                self.enable_disable_list(self.user_buttons, True)
            else:
                self.enable_disable_list(self.timed_user_buttons, True)
        except AttributeError:
            pass

    @staticmethod
    def enable_disable_list(elements_list, enable):
        for element in elements_list:
            element.setEnabled(enable)

    def modify_time_pushed(self):
        return self.parent_gui.modify_user_time(self.current_selected_user)

    def add_user_pushed(self):
        return self.parent_gui.add_user()

    def get_item_by_user_id(self, user_id):
        for item_i in range(self.adminUserListWidget.count()):
            item = self.adminUserListWidget.item(item_i)
            user = item.data(8)
            if user.id == user_id:
                return item

    def edit_user_pushed(self):
        return self.parent_gui.edit_user(self.current_selected_user)

    def delete_user_pushed(self):
        self.parent_gui.delete_user(self.current_selected_user)

    def refresh_clicked(self):
        self.add_users()

    @reload_last_user_after
    def add_users(self):
        self.adminUserListWidget.clear()
        self.add_items_to_users_list()

    def add_items_to_users_list(self):
        for item in self.make_list_items():
            self.adminUserListWidget.addItem(item)
        self.adminUserListWidget.sortItems(QtCore.Qt.AscendingOrder)

    def report_push_button_clicked(self):
        report = self.parent_gui.time_controller.generate_report(self.current_selected_user)
        self.ui.reportTableWidget.setRowCount(0)
        for report_items in self.make_report_items(report):
            row = self.ui.reportTableWidget.rowCount()
            self.ui.reportTableWidget.setRowCount(row + 1)
            for i, item in enumerate(report_items):
                self.ui.reportTableWidget.setItem(row, i, item)
        self.ui.reportTableWidget.sortByColumn(0, QtCore.Qt.DescendingOrder)

    @staticmethod
    def make_report_items(report):
        for day in report:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(day['date'])))
            items.append(QtWidgets.QTableWidgetItem(format_time(day['time_played'])[1]))
            items.append(QtWidgets.QTableWidgetItem(format_time(day['time_limit'])[1]))
            went_over, went_over_by = format_time(day['went_over_by'])
            if went_over:
                items.append(QtWidgets.QTableWidgetItem(f"-{went_over_by}"))
                for item in items:
                    item.setBackground(QtGui.QColor(102, 58, 61))
            else:
                items.append(QtWidgets.QTableWidgetItem(went_over_by))
            yield items

    def set_user_label(self, user):
        try:
            self.userLabel.setText(f"{user.name}")
            self.userLabel.setEnabled(True)
        except AttributeError:
            self.userLabel.setText("")
            self.userLabel.setEnabled(False)

    def make_list_items(self):
        for user in self.parent_gui.time_controller.current_users.values():
            item = QtWidgets.QListWidgetItem(user.name)
            try:
                if user.user_clock.state:
                    if user.is_time_up():
                        icon = QtGui.QIcon(resource_path("Graphics/over.png"))
                    else:
                        icon = QtGui.QIcon(resource_path("Graphics/active.png"))
                else:
                    icon = QtGui.QIcon(resource_path("Graphics/inactive.png"))
            except AttributeError:
                icon = QtGui.QIcon(resource_path("Graphics/inactive.png"))
            item.setIcon(icon)
            item.setData(8, user)
            yield item


class KeepSelectionWhenInactiveList(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(KeepSelectionWhenInactiveList, self).__init__(parent=parent)
        self.setStyleSheet(""" QListWidget::item:selected:!active { background: #287399;
                                                                    color: #eff0f1; 
                                                                    } """)


class SelectionListWidget(KeepSelectionWhenInactiveList):
    def __init__(self, parent=None):
        super(SelectionListWidget, self).__init__(parent=parent)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        super(SelectionListWidget, self).mousePressEvent(*args, *kwargs)
        super(SelectionListWidget, self).mouseDoubleClickEvent(*args, **kwargs)

    def mousePressEvent(self, *args, **kwargs):
        pass


class TimedUserWidgetSignals(QtCore.QObject):
    start_button_pushed = QtCore.pyqtSignal()


class TimedUserWidget(WidgetTemplate):
    def __init__(self, user, parent=None):
        super(TimedUserWidget, self).__init__(TimedUserWidgetUI.Ui_Form, parent=parent)
        self.current_user = user
        self.set_user_label(user)
        self.set_base_time_label(user)
        self.signals = TimedUserWidgetSignals()
        self.ui.startPushButton.clicked.connect(lambda: self.signals.start_button_pushed.emit())
        self.notification_manager = NotificationManager(self)
        self.reminder = Reminder(lambda: self.notification_manager.remind(self.current_user))
        self.reminder.start()
        self.set_start_button_text()
        self.ui.timeLabel.setStyleSheet("QLabel { border: 2px solid black; }")
        self.timer = QtCore.QElapsedTimer()
        self.emitter = QtCore.QTimer()
        self.make_timers()
        self.last_time_left = timedelta(seconds=0)
        self.last_time = None
        self.last_state = None
        self.last_notify_state = None
        self.update_time(self.current_user)

    @property
    def time_left(self):
        try:
            time_elapsed = self.timer.elapsed() if self.timer.isValid() else 0
            return self.last_time_left - timedelta(milliseconds=time_elapsed)
        except AttributeError:
            return timedelta(milliseconds=0)

    def start_button_clicked(self):
        self.signals.start_button_pushed.emit()

    def set_start_button_text(self):
        try:
            self.startPushButton.setEnabled(True)
            if self.last_state:
                if self.ui.startPushButton.text() != "Stop":
                    self.startPushButton.setText("Stop")
                    self.startPushButton.setStyleSheet(" QPushButton { background-color: rgba(193, 66, 66, 0.37); }")
                    self.notification_manager.reset()
                    self.notification_manager.interacted(self.current_user)
            else:
                if self.ui.startPushButton.text() != "Start":
                    self.startPushButton.setText("Start")
                    self.startPushButton.setStyleSheet(" QPushButton { background-color: rgba(72, 191, 63, 0.32); }")
                    self.notification_manager.reset()
                    self.notification_manager.interacted(self.current_user)
        except AttributeError:
            self.startPushButton.setText("Start")
            self.startPushButton.setStyleSheet(" QPushButton { background-color: rgba(72, 191, 63, 0.32); }")

    def set_user_label(self, user):
        try:
            self.userLabel.setText(f"{user.name}")
            self.userLabel.setEnabled(True)
        except AttributeError:
            self.userLabel.setText(f"")
            self.userLabel.setEnabled(False)

    def set_base_time_label(self, user):
        try:
            self.baseTimeLabel.setText(f"Time Limit: {user.play_time}")
            self.baseTimeLabel.setEnabled(True)
        except AttributeError:
            self.baseTimeLabel.setText(f"Time Limit:")
            self.baseTimeLabel.setEnabled(False)

    def set_time_label_color(self):
        state = self.current_user.get_state_from_time_left(self.time_left.total_seconds()/60)
        try:
            if state == "times_up" != self.last_notify_state:
                self.timeLabel.setStyleSheet(self.timeLabel.styleSheet() +
                                             " QLabel { color: #fc0303; } ")
                self.notification_manager.check_alarm(self.current_user)
            elif state == "warning" != self.last_notify_state:
                self.timeLabel.setStyleSheet(self.timeLabel.styleSheet() +
                                             " QLabel { color: #EA6500; } ")
                self.notification_manager.check_warning(self.current_user)
            elif state == "idle" != self.last_notify_state:
                self.timeLabel.setStyleSheet(self.timeLabel.styleSheet() +
                                             " QLabel { color: #ffffff; } ")
            self.last_notify_state = state
        except AttributeError:
            self.timeLabel.setStyleSheet("QLabel { border: 2px solid black; }")
            self.timeLabel.setEnabled(False)

    def set_time(self):
        try:
            negative, formatted_time = format_time(self.time_left)
            if negative:
                self.timeLabel.setText(f"Went Over: {formatted_time}")
            else:
                self.timeLabel.setText(f"Time Left: {formatted_time}")
            self.timeLabel.setEnabled(True)
        except AttributeError:
            self.timeLabel.setText(f"Time Left:")
        self.set_time_label_color()
        self.set_start_button_text()

    def make_timers(self):
        self.emitter.setInterval(100)
        self.emitter.timeout.connect(self.set_time)
        self.timer = QtCore.QElapsedTimer()

    def reset_timers(self):
        self.emitter.stop()
        self.make_timers()

    def sync_with_user(self, user):
        self.current_user = user
        self.notification_manager.reset()
        self.last_time_left = self.current_user.time_left()
        self.last_time = [t for t in user.user_clock.current_time_set]
        self.reset_timers()
        self.last_state = self.current_user.user_clock.state
        if self.last_state:
            self.timer.start()
            self.emitter.start()
        self.set_time()

    def update_time(self, user):
        time_set = [t for t in user.user_clock.current_time_set]
        discrepancy = self.time_left - user.time_left()
        if time_set != self.last_time or user != self.current_user or not self.is_acceptable_discrepancy(discrepancy):
            self.sync_with_user(user)

    @staticmethod
    def is_acceptable_discrepancy(discrepancy):
        return -.1 <= discrepancy.total_seconds() <= .1


class CrashReportDialog(DialogTemplate):
    def __init__(self, parent=None):
        super(CrashReportDialog, self).__init__(CrashReportUI.Ui_Dialog, parent)
        self.ui.sendPushButton.clicked.connect(self.accept)
        self.ui.cancelPushButton.clicked.connect(self.close)
        self.ui.sendPushButton.setEnabled(False)
        self.ui.reportTextEdit.textChanged.connect(self.report_line_edit_changed)

    def report_line_edit_changed(self):
        self.ui.sendPushButton.setEnabled(self.ui.reportTextEdit.toPlainText().strip() != "")


def are_you_sure_prompt(msg):
    dialog = AreYouSureDialog(msg)
    dialog.exec()
    return dialog.result()


def error_dialog(msg):
    ErrorDialog(msg)
    ErrorDialog.exec()


def format_time(time_delta):
    seconds = int(time_delta.total_seconds())
    negative = False
    if seconds < 0:
        negative = True
        seconds *= -1
    hours = int(seconds / 3600)
    seconds = seconds - (hours*3600)
    minutes = int(seconds / 60)
    seconds = seconds - (minutes*60)
    return negative, f"{hours}:{minutes:02}:{seconds:02}"
