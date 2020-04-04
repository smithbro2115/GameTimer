from PyQt5 import QtCore, QtWidgets
from GUI import MainWindowUI
import qdarkstyle
from TimeController import TimeController
from GUI.CustomGUI import GUIMessageController
from GUI import CustomGUI, CustomGuiModules
from Utils.UsefulUtils import reload_after


class Gui(MainWindowUI.Ui_MainWindow):
    def __init__(self):
        self.main_window = None
        self.time_controller = None
        self.gui_message_controller = None
        self.current_user_view = None
        self.admin_dialog = False
        self.path_not_found_dialog = False
        self.userListWidget = CustomGuiModules.SelectionListWidget()

    def setup_additional(self, main_window):
        self.main_window = main_window
        self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.verticalLayout.insertWidget(0, self.userListWidget)
        self.userListWidget.setMinimumWidth(175)
        self.userListWidget.setMaximumWidth(175)
        self.gui_message_controller = GUIMessageController(self)
        self.time_controller = TimeController(self)
        self.time_controller.load()
        self.time_controller.get_last_user()
        self.userListWidget.itemDoubleClicked.connect(lambda x: self.time_controller.switch_user(x.data(8)))
        self.logOutPushButton.clicked.connect(self.log_out_button_pushed)
        self.actionNew_User.triggered.connect(self.new_user_triggered)
        self.actionDelete_User.triggered.connect(self.delete_user_triggered)
        self.actionEdit_User.triggered.connect(self.edit_user_triggered)
        self.actionGlobal_Settings.triggered.connect(self.global_settings_triggered)

    def new_user_triggered(self):
        self.add_user()

    @reload_after
    def add_user(self):
        if self.authorize():
            return CustomGUI.new_user_triggered(self)

    def no_admin(self):
        if not self.admin_dialog:
            self.admin_dialog = True
            user = CustomGUI.new_user_triggered(self, admin_only=True)
            self.admin_dialog = False
            if not user:
                self.no_admin()
            else:
                self.time_controller.reload()

    def reset(self):
        self.gui_message_controller = GUIMessageController(self)
        self.time_controller = TimeController(self)

    def updated_remotely(self):
        try:
            last_user = self.time_controller.current_user.id
        except AttributeError:
            last_user = None
        self.reset()
        self.time_controller.load()
        try:
            self.time_controller.switch_user(self.time_controller.current_users[last_user])
            self.userListWidget.setCurrentItem(self.get_list_item_from_id(last_user))
        except KeyError:
            self.time_controller.switch_user(last_user)

    def delete_user_triggered(self):
        user = self.userListWidget.currentItem().data(8)
        self.delete_user(user)

    @reload_after
    def delete_user(self, user):
        if self.authorize():
            return CustomGUI.delete_user_triggered(self, user)

    @reload_after
    def modify_user_time(self, user):
        if self.authorize():
            return CustomGUI.modify_time_triggered(self, user)

    def edit_user_triggered(self):
        user = self.userListWidget.currentItem().data(8)
        self.edit_user(user)

    @reload_after
    def edit_user(self, user):
        if self.authorize():
            return CustomGUI.edit_user_triggered(self, user)

    def global_settings_triggered(self):
        self.change_global_setting()

    @reload_after
    def change_global_setting(self):
        if self.authorize():
            return CustomGUI.change_global_settings(self)

    def reload_admin(self):
        self.gui_message_controller.users_loaded()

    def load_users(self, users):
        self.remove_all_items_from_users_list()
        list_items = list(CustomGUI.make_list_items_from_users(users))
        self.add_items_to_users_list(list_items)
        self.gui_message_controller.users_loaded()
        # self.userListWidget.setSel

    def add_items_to_users_list(self, items):
        for item in items:
            self.userListWidget.addItem(item)
        self.userListWidget.sortItems(QtCore.Qt.AscendingOrder)

    def log_in(self, user):
        return CustomGUI.log_in(self, user)

    def log_out_button_pushed(self):
        self.time_controller.switch_user(None)
        self.userListWidget.clearSelection()

    def authorize(self):
        try:
            if self.time_controller.current_user.has_permission():
                return True
        except AttributeError:
            pass
        CustomGUI.you_are_not_authorized_msg(self)

    def start_button_clicked(self):
        try:
            self.time_controller.interact()
            self.gui_message_controller.time_updated(self.time_controller.current_user)
        except (FileNotFoundError, PermissionError):
            pass

    def remove_all_items_from_users_list(self):
        self.userListWidget.clear()

    def connect_time_checker_signals(self, time_checker):
        self.gui_message_controller.connect_time_checker_signals(time_checker)

    def get_list_item_from_id(self, user_id):
        for item_i in range(self.userListWidget.count()):
            item = self.userListWidget.item(item_i)
            if item.data(8).id == user_id:
                return item

    def users_folder_could_not_be_found(self):
        if not self.path_not_found_dialog:
            self.path_not_found_dialog = True
            dialog = CustomGuiModules.PathNotFoundDialog()
            result = dialog.exec()
            if result:
                if dialog.state == "new_path":
                    CustomGUI.get_new_users_path()
                self.path_not_found_dialog = False
                self.time_controller.load()
                self.time_controller.get_last_user()
            else:
                sys.exit()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, gui_ui):
        super(MainWindow, self).__init__()
        self.ui = gui_ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Gui()
    mainWindow = MainWindow(ui)
    ui.setupUi(mainWindow)
    ui.setup_additional(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
