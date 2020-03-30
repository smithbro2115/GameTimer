import os
from platform import system
import pathlib


def make_folder_if_it_does_not_exist(src, folder):
    new_src = src.replace('\\', '/')
    directory = f"{new_src}/{folder}"
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass
    return directory


def get_app_data_folder(folder):
    if system() == 'Windows':
        app_data_path = os.getenv('APPDATA')
    else:
        app_data_path = os.path.expanduser('~/Documents')
    clocking_path = make_folder_if_it_does_not_exist(app_data_path, 'Video Game Time')
    return make_folder_if_it_does_not_exist(clocking_path, folder)


def get_parent_dir(path):
    return pathlib.Path(path).parent


def add_file_if_it_does_not_exist(path):
    open(path, 'a').close()


def delete_directory(directory):
    import shutil
    try:
        shutil.rmtree(directory)
        return True
    except Exception:
        return False


def resource_path(relative_path):
    import sys
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
