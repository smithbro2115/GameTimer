import configparser
from Utils.FileUtils import get_app_data_folder, add_file_if_it_does_not_exist
import csv
from configparser import NoOptionError, NoSectionError


def get_users_folder():
    try:
        users_folder = read_from_config("SETTINGS", "users_path")
    except (NoOptionError, NoSectionError):
        users_folder = get_app_data_folder('users')
        add_to_config("SETTINGS", "users_path", users_folder)
    return users_folder


def add_to_config(category, option, value):
    config_path = f"{get_app_data_folder('')}/config.ini"
    write_to_ini_file(category, option, value, config_path)


def try_to_read_from_config(category, option):
    try:
        return read_from_config(category, option)
    except (configparser.NoSectionError, configparser.NoOptionError):
        return None


def try_to_add_section_to_config(ini_file, section):
    try:
        ini_file.add_section(section)
    except configparser.DuplicateSectionError:
        pass


def read_from_config(category, option):
    config_path = f"{get_app_data_folder('')}/config.ini"
    return read_from_ini_file(category, option, config_path)


def write_to_ini_file(category, option, value, path):
    cache = configparser.ConfigParser()
    try_to_add_section_to_config(cache, category)
    cache.read(path)
    cache.set(category, str(option), str(value))
    with open(path, 'w') as cache_file:
        cache.write(cache_file)


def read_from_ini_file(category, option, path):
    cache = configparser.ConfigParser()
    cache.read(path)
    return cache.get(category, option)


def try_to_read_from_ini_file(category, option, path):
    try:
        return read_from_ini_file(category, option, path)
    except (configparser.NoSectionError, configparser.NoOptionError):
        return None


def write_to_cache(category, option, value):
    cache_path = f"{get_app_data_folder('')}/cache.ini"
    write_to_ini_file(category, option, value, cache_path)


def read_from_cache(category, option):
    cache_path = f"{get_app_data_folder('')}/cache.ini"
    return read_from_ini_file(category, option, cache_path)


def add_to_csv_file(path, list_to_write, replace):
    new_list = get_list_from_csv(path)
    if replace:
        new_list.pop()
    new_list.append(list_to_write)
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in new_list:
            writer.writerow(row)


def save_list_to_csv(path, list_to_write):
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in list_to_write:
            writer.writerow(row)


def add_to_list_if_name_not_duplicate(dict_list, new_dict, keyword):
    for existing in dict_list:
        if existing[keyword] == new_dict[keyword]:
            break
    else:
        dict_list.append(new_dict)
    return dict_list


def add_dict_to_list_csv_file(path, dict_to_write, keyword='name'):
    list_of_dicts = get_dicts_from_csv(path)
    add_to_list_if_name_not_duplicate(list_of_dicts, dict_to_write, keyword)
    save_dicts_to_csv_file(path, list_of_dicts)


def save_dict_to_csv_file(path, dict_to_write):
    try:
        headers = dict_to_write.keys()
    except IndexError:
        headers = {}
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerow(dict_to_write)


def add_to_dict_from_csv_file(path, dict_):
    existing_dict = read_dict_from_csv_file(path)
    for key, value, in dict_.items():
        existing_dict[key] = value
    save_dict_to_csv_file(path, existing_dict)


def read_dict_from_csv_file(path):
    add_file_if_it_does_not_exist(path)
    with open(path, mode='r') as file:
        dict_ = csv.DictReader(file)
        new_dict = {}
        for row in dict_:
            for key, value in dict(row).items():
                new_dict[key] = value
        return new_dict


def save_dicts_to_csv_file(path, dicts_to_save):
    try:
        headers = dicts_to_save[0].keys()
    except IndexError:
        headers = {}
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(dicts_to_save)


def replace_dicts_from_csv(path, old_dict, new_dict):
    delete_dict_from_csv(path, old_dict)
    add_dict_to_list_csv_file(path, new_dict)


def delete_dict_from_csv(path, dict_to_delete):
    list_of_dicts = get_dicts_from_csv(path)
    for existing_dict in list_of_dicts:
        if existing_dict == dict_to_delete:
            list_of_dicts.remove(existing_dict)
            save_dicts_to_csv_file(path, list_of_dicts)
            return True
    return False


def get_list_from_csv(path):
    with open(path, mode='r') as file:
        return list(csv.reader(file))


def get_dicts_from_csv(path):
    with open(path, mode='r') as file:
        raw_dicts = csv.DictReader(file)
        list_of_dicts = []
        for raw_dict in raw_dicts:
            list_of_dicts.append(dict(raw_dict))
        return list_of_dicts
