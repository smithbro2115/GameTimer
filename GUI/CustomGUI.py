from PyQt5 import QtWidgets, QtCore, QtGui
from GUI.CustomGuiModules import NewUserDialog, are_you_sure_prompt, SettingsDialog, LogInDialog
from GUI import CustomGuiModules
from Utils import CachingUtils, FileUtils
from configparser import NoOptionError, NoSectionError
from Users import create_user, delete_user, edit_user
from datetime import timedelta


class GUIMessageController:
    def __init__(self, parent):
        self.thread_pool = QtCore.QThreadPool()
        self.parent = parent
        self.widget = QtWidgets.QWidget()
        self.parent.viewerWidget.layout().addWidget(self.widget)

    def connect_time_checker_signals(self, time_checker):
        time_checker.signals.update_time_left.connect(self.time_updated)

    def time_updated(self, user):
        try:
            self.widget.update_time(user)
        except (AttributeError, PermissionError, OSError):
            pass

    def users_loaded(self):
        try:
            self.widget.add_users()
        except AttributeError:
            pass

    def user_edited(self):
        try:
            self.widget.reload_user()
        except AttributeError:
            pass

    def user_switched(self, user):
        try:
            if user.user_type == "timed_user":
                widget = CustomGuiModules.TimedUserWidget(user)
                widget.signals.start_button_pushed.connect(self.parent.start_button_clicked)
                self.replace_widget(widget)
            else:
                widget = CustomGuiModules.AdminUserWidget(user, self.parent)
                self.replace_widget(widget)
        except AttributeError:
            widget = QtWidgets.QWidget()
            self.replace_widget(widget)
            
    def replace_widget(self, new_widget):
        self.clear_viewer()
        self.parent.viewerWidget.layout().addWidget(new_widget)
        self.widget = new_widget

    def clear_viewer(self):
        layout = self.parent.viewerWidget.layout()
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)
        if not self.parent.main_window.isMaximized():
            self.parent.viewerWidget.adjustSize()
            self.parent.centralwidget.adjustSize()
            self.parent.main_window.adjustSize()


def new_user_triggered(parent, admin_only=False):
    dialog = NewUserDialog(parent=parent.main_window, admin_only=admin_only)
    dialog.exec()
    if dialog.result():
        warning_time = dialog.ui.warningTimeLineEdit.text()
        if warning_time.strip() == "":
            warning_time = 0
        user_type = 'timed_user'
        if dialog.ui.adminCheckBox.isChecked():
            user_type = 'admin'
        password = None
        if dialog.ui.passwordLineEdit.text() != "":
            password = dialog.ui.passwordLineEdit.text()
        info = {'name': dialog.ui.nameLineEdit.text(), 'base_time': f"{dialog.ui.baseTimeLineEdit.text()}m",
                'follow_global': dialog.ui.followGlobalCheckBox.isChecked(), 'user_type': user_type,
                'warning_time': int(warning_time), 'password': password}
        return create_user(info)


def delete_user_triggered(parent, user):
    if are_you_sure_prompt(f"Are you sure you want to delete the user: {user.name}"):
        if user == parent.time_controller.current_user:
            parent.time_controller.reset()
        del parent.time_controller.current_users[user.id]
        delete_user(user)
        return user


def modify_time_triggered(parent, user):
    dialog = CustomGuiModules.ModifyTimeDialog(user, parent=parent.main_window)
    dialog.exec()
    if dialog.result():
        user.play_time += timedelta(minutes=dialog.ui.timeSpinBox.value())
        return user


def edit_user_triggered(parent, user):
    info = user.info
    dialog = NewUserDialog(parent=parent.main_window, edit=True, **info)
    dialog.exec()
    if dialog.result():
        warning_time = dialog.ui.warningTimeLineEdit.text()
        if warning_time.strip() == "":
            warning_time = 0
        user_type = 'timed_user'
        if dialog.ui.adminCheckBox.isChecked():
            user_type = 'admin'
        info['name'] = dialog.ui.nameLineEdit.text()
        info['base_time'] = f"{dialog.ui.baseTimeLineEdit.text()}m"
        info['follow_global'] = dialog.ui.followGlobalCheckBox.isChecked()
        info['warning_time'] = int(warning_time)
        info['user_type'] = user_type
        password = dialog.ui.passwordLineEdit.text()
        if password != "":
            info['password'] = dialog.ui.passwordLineEdit.text()
        else:
            info['password'] = None
        return edit_user(info, user)


def change_global_settings(parent):
    prior_settings = {'global_time': CachingUtils.try_to_read_from_config("GLOBAL_SETTINGS", "global_time"),
                      "global_warning_time": CachingUtils.try_to_read_from_config("GLOBAL_SETTINGS", "global_warning_time"),
                      "users_path": CachingUtils.try_to_read_from_config("SETTINGS", "users_path")}
    dialog = SettingsDialog(parent=parent.main_window, **prior_settings)
    dialog.exec()
    if dialog.result():
        global_time = dialog.ui.globalTimeLineEdit.text()
        global_warning_time = dialog.ui.globalWarningTimeLineEdit.text()
        users_path = dialog.ui.usersPathLineEdit.text()
        if global_time.strip() == "":
            global_time = 0
        if global_warning_time.strip() == "":
            global_warning_time = 0
        CachingUtils.add_to_config("GLOBAL_SETTINGS", "global_time", f"{global_time}m")
        CachingUtils.add_to_config("GLOBAL_SETTINGS", "global_warning_time", f"{global_warning_time}")
        CachingUtils.add_to_config("SETTINGS", "users_path", users_path)
        return True


def get_new_users_path():
    new_path_dialog = CustomGuiModules.GetFolderLocationDialog(FileUtils.get_app_data_folder("users"))
    result = new_path_dialog.get_folder_path()
    if result != "":
        CachingUtils.add_to_config("SETTINGS", "users_path", result)
        return result


def log_in(parent, user):
    try:
        if user.password:
            dialog = LogInDialog(user.name, user.password, parent.main_window)
            dialog.exec()
            if dialog.result():
                return True
        else:
            return True
    except AttributeError:
        return True


def make_list_items_from_users(users):
    for user in users.values():
        item = QtWidgets.QListWidgetItem(user.name)
        item.setData(8, user)
        yield item


def you_are_not_authorized_msg(parent):
    msg = "Sorry but you are not allowed to do this. Please log in to an admin account to continue"
    dialog = CustomGuiModules.ErrorDialog(msg, window_label="Not Authorized", parent=parent.main_window)
    dialog.exec()

