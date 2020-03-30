from Utils import CachingUtils, FileUtils
from datetime import datetime


def convert_string_to_bool(string):
    string = str(string)
    if string.lower() == "true":
        return True
    elif string.lower() == "false":
        return False
    else:
        raise ValueError("String must either be true or false")


def reload_after(function):
    def wrapper(*args, **kwargs):
        self = args[0]
        is_current_user, last_user_id, reload_admin, changed_user_id = get_is_current_and_others(*args)
        result = function(*args, **kwargs)
        if result:
            load_time = self.time_controller.reload()
            if is_current_user and last_user_id:
                try:
                    self.time_controller.switch_user(self.time_controller.current_users[last_user_id])
                except AttributeError:
                    pass
            elif reload_admin:
                self.reload_admin()
            self.userListWidget.setCurrentItem(self.get_list_item_from_id(last_user_id))
            write_to_user_edited_notify_file(load_time)
            return result
    return wrapper


def catch_deletion(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except (FileNotFoundError, PermissionError):
            pass
    return wrapper


def write_to_user_edited_notify_file(date_time):
    edit_notifier_path = f'{CachingUtils.get_users_folder()}/edit_notifier.csv'
    FileUtils.add_file_if_it_does_not_exist(edit_notifier_path)
    CachingUtils.add_to_dict_from_csv_file(edit_notifier_path, {'date_time': date_time})


def read_from_user_edited_notify_file():
    edit_notifier_path = f'{CachingUtils.get_users_folder()}/edit_notifier.csv'
    try:
        return datetime.strptime(CachingUtils.read_dict_from_csv_file(edit_notifier_path)['date_time'],
                                 '%Y-%m-%d %H:%M:%S.%f')
    except (FileNotFoundError, KeyError):
        write_to_user_edited_notify_file(datetime.now())
        return read_from_user_edited_notify_file()


def get_is_current_and_others(*args):
    self = args[0]
    reload_admin = False
    is_current_user = False
    changed_user_id = None
    try:
        last_user_id = self.time_controller.current_user.id
        changed_user_id = args[1].id
        is_current_user = last_user_id == changed_user_id
    except AttributeError:
        last_user_id = None
        is_current_user = False
    except IndexError:
        last_user = self.time_controller.current_user
        last_user_id = last_user.id
        if last_user.user_type != "admin":
            is_current_user = True
        else:
            reload_admin = True
    return is_current_user, last_user_id, reload_admin, changed_user_id
