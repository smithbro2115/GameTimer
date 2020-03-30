from Utils.FileUtils import delete_directory
from Utils import CachingUtils, FileUtils, UsefulUtils
import Clocks
import os
from pytimeparse.timeparse import timeparse
from datetime import timedelta
from configparser import NoSectionError, NoOptionError


class User:
    def __init__(self, file_path, **kwargs):
        self.file_path = file_path
        self.dir = os.path.dirname(self.file_path)
        self.info = kwargs
        self.name = kwargs['name']
        self.id = kwargs['id']
        self.user_type = kwargs['user_type']
        self.logged_in = False

    @property
    def name(self):
        return self.info['name']

    @name.setter
    def name(self, value):
        self.info['name'] = value

    @property
    def id(self):
        return self.info['id']

    @id.setter
    def id(self, value):
        self.info['id'] = value

    @property
    def password(self):
        return self.info['password']

    @password.setter
    def password(self, value):
        self.info['password'] = value

    def has_permission(self):
        if self.user_type == 'admin':
            return True

    def save(self):
        CachingUtils.save_dict_to_csv_file(self.file_path, self.info)


class TimedUser(User):
    def __init__(self, file_path, **kwargs):
        super(TimedUser, self).__init__(file_path, **kwargs)
        self.clock_file_path = f"{self.dir}/clock.csv"
        self.time_limit_file_path = f"{self.dir}/time_limit.csv"
        self.base_time_file_path = f"{self.dir}/base_time.csv"
        self.user_clock = Clocks.UserClock(self.clock_file_path)
        self.time_limit = Clocks.TimeLimit(self.time_limit_file_path, self.base_time, self.base_time_file_path)

    @property
    def state(self):
        if self.is_warning_time():
            return 'warning'
        elif self.is_time_up():
            return 'times_up'
        elif self.user_clock.state:
            return 'using_time'
        else:
            return 'idle'

    @property
    def base_time(self):
        if not UsefulUtils.convert_string_to_bool(self.info['follow_global']):
            return timedelta(seconds=timeparse(self.info['base_time']))
        else:
            try:
                global_setting = CachingUtils.read_from_config("GLOBAL_SETTINGS", "global_time")
                return timedelta(seconds=timeparse(global_setting))
            except (NoSectionError, NoOptionError):
                return timedelta(seconds=3600)

    @base_time.setter
    def base_time(self, value):
        self.info['base_time'] = value

    @property
    def play_time(self):
        return self.time_limit.time_limit_for_today

    @play_time.setter
    def play_time(self, value: timedelta):
        self.time_limit.add_time_to_limit((timedelta() - self.play_time) + value)

    @property
    def warning_time(self):
        if not UsefulUtils.convert_string_to_bool(self.info['follow_global']):
            return int(self.info['warning_time'])
        else:
            try:
                return int(CachingUtils.read_from_config("GLOBAL_SETTINGS", "global_warning_time"))
            except (NoSectionError, NoOptionError):
                return 0

    @warning_time.setter
    def warning_time(self, value):
        self.info['warning_time'] = value

    def is_warning_time(self):
        return self.warning_time >= self.time_left_in_minutes() >= 0

    def is_time_up(self):
        return self.time_left().total_seconds() <= 0

    def time_left(self):
        return self.play_time - self.user_clock.total_time_spent_today

    def time_left_in_minutes(self):
        return self.time_left().total_seconds()/60


def delete_user(user):
    return delete_directory(FileUtils.get_parent_dir(user.file_path))


def load_users():
    users_folder = CachingUtils.get_users_folder()
    FileUtils.make_folder_if_it_does_not_exist(users_folder, "")
    user_directories = os.listdir(users_folder)
    users = []
    for user_directory in user_directories:
        user_path = f"{users_folder}/{user_directory}/user_info.csv"
        if os.path.isfile(user_path):
            user_info = CachingUtils.read_dict_from_csv_file(user_path)
            try:
                if user_info['user_type'] == 'timed_user':
                    users.append(TimedUser(user_path, **user_info))
                else:
                    users.append(User(user_path, **user_info))
            except KeyError:
                pass
    return users


def find_unique_id():
    users_folder = CachingUtils.get_users_folder()
    i = 0
    while True:
        new_id = f"user_{i:02}"
        if not os.path.exists(f"{users_folder}/{new_id}"):
            return new_id
        i += 1


def create_user(info):
    info['id'] = find_unique_id()
    users_folder = CachingUtils.get_users_folder()
    FileUtils.make_folder_if_it_does_not_exist(users_folder, info['id'])
    user = User(f"{users_folder}/{info['id']}/user_info.csv", **info)
    user.save()
    return user


@UsefulUtils.catch_deletion
def edit_user(info, user):
    user.__init__(user.file_path, **info)
    user.save()
    return user


# test_user = create_user({'name': "Joshua", 'user_type': 'timed_user', 'base_time': "1:00:00", "warning_time": 5,
#                          'follow_global': False})
# print(test_user.info)
# test_user = load_users()[0]
# test_user.user_clock.interact()
