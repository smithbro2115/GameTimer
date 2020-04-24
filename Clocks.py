from datetime import datetime, timedelta
from Utils import CachingUtils, FileUtils


class UserClock:
    def __init__(self, file_path):
        self.state = False
        self.current_time_set = []
        self._total_time_spent_today = timedelta()
        self.file_path = file_path
        self.load()

    @property
    def total_time_spent_today(self):
        self.load()
        if len(self.current_time_set) == 1:
            stop_time = datetime.now()
            if stop_time.date() == self.current_time_set[0].date():
                time_since_start = datetime.now() - self.current_time_set[0]
                return self._total_time_spent_today + time_since_start
            else:
                start_time = datetime.strptime(f"{stop_time.day} {stop_time.month} {stop_time.year}",
                                                   "%d %m %Y")
                return stop_time - start_time
        else:
            return self._total_time_spent_today

    @total_time_spent_today.setter
    def total_time_spent_today(self, value):
        self._total_time_spent_today = value

    @property
    def history(self):
        return self.group_time_spent_into_days(self.get_all_time())

    def interact(self):
        self.load()
        if self.state:
            return self.stop()
        else:
            return self.start()

    def start(self):
        date_time = datetime.now()
        self.current_time_set = [date_time]
        self.state = True
        self.save()
        return date_time

    def stop(self):
        date_time = datetime.now()
        self.current_time_set.append(date_time)
        self.state = False
        self.save(replace=True)
        self.reset()
        return date_time

    def save(self, replace=False):
        CachingUtils.add_to_csv_file(self.file_path, self.current_time_set, replace)

    def load(self):
        self.reset()
        rows = CachingUtils.get_list_from_csv(self.file_path)
        self.interpret_rows(rows)

    def get_all_time(self):
        rows = CachingUtils.get_list_from_csv(self.file_path)
        return self.parse_rows(rows)

    def interpret_rows(self, rows):
        time_sets = self.parse_rows_from_today(rows)
        try:
            if self.check_if_clocked_in(time_sets[0]):
                self.state = True
                self.current_time_set = time_sets[0]
                time_sets.pop(0)
        except IndexError:
            pass
        self.total_time_spent_today = self.get_total_time_from_time_sets(time_sets, datetime.now().date())

    @staticmethod
    def get_total_time_from_time_sets(time_sets, date):
        total_time = timedelta()
        for time_set in time_sets:
            start_datetime = time_set[0]
            try:
                stop_datetime = time_set[1]
            except IndexError:
                stop_datetime = datetime.now()
            if start_datetime.date() != date:
                start_datetime = datetime.strptime(f"{stop_datetime.day} {stop_datetime.month} {stop_datetime.year}",
                                                   "%d %m %Y")
            if stop_datetime.date() != date:
                stop_datetime = datetime.strptime(f"{start_datetime.day} {start_datetime.month} {start_datetime.year} "
                                                   f"23 59 59",
                                                   "%d %m %Y %H %M %S")
            total_time += stop_datetime - start_datetime
        return total_time

    @staticmethod
    def parse_rows(rows):
        parsed_rows = []
        for row in rows:
            parsed_row = [datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')]
            try:
                parsed_row.append(datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f'))
                parsed_rows.append(parsed_row)
            except IndexError:
                parsed_rows.append(parsed_row)
        return parsed_rows

    def group_time_spent_into_days(self, time_sets):
        days_and_time_sets = self.group_all_time_sets_into_days(time_sets)
        days_and_time_spent = {}
        for date, times in days_and_time_sets.items():
            try:
                days_and_time_spent[date] += self.get_total_time_from_time_sets(times, date)
            except KeyError:
                days_and_time_spent[date] = self.get_total_time_from_time_sets(times, date)
        return days_and_time_spent

    def group_all_time_sets_into_days(self, time_sets):
        days_and_time_sets = {}
        for time_set in time_sets:
            for day in self.get_all_days_from_time_set(time_set):
                try:
                    days_and_time_sets[day].append(time_set)
                except KeyError:
                    days_and_time_sets[day] = [time_set]
        return days_and_time_sets

    @staticmethod
    def get_all_days_from_time_set(time_set):
        start_date = time_set[0].date()
        try:
            stop_date = time_set[1].date()
        except IndexError:
            stop_date = datetime.now().date()
            time_set.append(datetime.now())
        total_days = int((stop_date - start_date).total_seconds()/60/60/24)+1
        for i in range(total_days):
            yield time_set[0].date() + timedelta(days=i)

    @staticmethod
    def parse_rows_from_today(rows):
        parsed_rows = []
        for row in reversed(rows):
            parsed_row = [datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')]
            try:
                parsed_row.append(datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f'))
                if parsed_row[1].date() == datetime.now().date() or parsed_row[0].date() == datetime.now().date():
                    parsed_rows.append(parsed_row)
                else:
                    break
            except IndexError:
                parsed_rows.append(parsed_row)
        return parsed_rows

    @staticmethod
    def check_if_clocked_in(row):
        return len(row) == 1

    def reset(self):
        FileUtils.add_file_if_it_does_not_exist(self.file_path)
        self.state = False
        self.current_time_set = []


class TimeLimit:
    def __init__(self, file_path, base_time, base_time_file_path):
        self.file_path = file_path
        self.base_time_file_path = base_time_file_path
        FileUtils.add_file_if_it_does_not_exist(self.base_time_file_path)
        self.base_time = int(base_time.total_seconds()/60)
        self.rows = []

    @property
    def time_limit_for_today(self):
        return self.interpret_times_for_today() + self.base_time

    @property
    def base_times(self):
        return CachingUtils.read_dict_from_csv_file(self.base_time_file_path)

    @property
    def base_time(self):
        base_time_dict = CachingUtils.read_dict_from_csv_file(self.base_time_file_path)
        base_time_string = list(base_time_dict.values())[-1]
        return timedelta(minutes=int(base_time_string))

    @base_time.setter
    def base_time(self, value: int):
        self.add_to_csv_if_different(value)

    def add_to_csv_if_different(self, base_time):
        base_time_dict = CachingUtils.read_dict_from_csv_file(self.base_time_file_path)
        if timedelta(minutes=base_time) != timedelta(minutes=int(list(base_time_dict.values())[-1])):
            new_base_time = {datetime.now().date(): base_time}
            CachingUtils.add_to_dict_from_csv_file(self.base_time_file_path, new_base_time)

    @property
    def history(self):
        self.load()
        time_mod_rows = self.rows
        time_mods = self.parse_rows(time_mod_rows)
        base_time_rows = self.convert_base_time_limits_to_rows(self.base_times)
        base_times = self.parse_rows(base_time_rows)
        return self.group_time_limits_into_days(list(base_times), self.group_time_mods_into_days(time_mods))

    def add_time_to_limit(self, time_to_add: timedelta):
        date_time = datetime.now()
        new_row = [date_time, int(time_to_add.total_seconds())]
        self.save(new_row)
        return new_row

    def save(self, row, replace=False):
        try:
            CachingUtils.add_to_csv_file(self.file_path, row, replace)
        except FileNotFoundError:
            FileUtils.add_file_if_it_does_not_exist(self.file_path)
            self.save(row, replace)

    def load(self):
        self.reset()
        self.rows = CachingUtils.get_list_from_csv(self.file_path)

    def interpret_times_for_today(self):
        self.load()
        parsed_rows = self.parse_rows_for_today(self.rows, datetime.now().day)
        return self.add_times_together(row[1] for row in parsed_rows)

    @staticmethod
    def group_time_mods_into_days(time_mods):
        date_and_times = {}
        for time_mod in time_mods:
            date = time_mod[0].date()
            try:
                date_and_times[date] += time_mod[1]
            except KeyError:
                date_and_times[date] = time_mod[1]
        return date_and_times

    def group_time_limits_into_days(self, base_times, time_modifications):
        days = {}
        for i, (base_time_day, base_time) in enumerate(base_times):
            days[base_time_day.date()] = self.make_day(base_time,
                                         self.try_to_get_time_modification(time_modifications, base_time_day))
            day = base_time_day + timedelta(days=1)
            while True:
                try:
                    if day >= base_times[i+1][0]:
                        break
                except IndexError:
                    today = datetime.now()
                    if day > datetime(today.year, today.month, today.day):
                        break
                days[day.date()] = self.make_day(base_time, self.try_to_get_time_modification(time_modifications, day))
                day += timedelta(days=1)
        return days

    @staticmethod
    def try_to_get_time_modification(time_modifications, day):
        try:
            return time_modifications[day.date()]
        except KeyError:
            return timedelta(seconds=0)

    @staticmethod
    def make_day(base_time, time_mods):
        return base_time + time_mods

    @staticmethod
    def convert_base_time_limits_to_rows(base_time_limits):
        rows = []
        for key, value in base_time_limits.items():
            row = [key, value]
            rows.append(row)
        return rows

    @staticmethod
    def add_times_together(mods):
        total_mod_time = timedelta()
        for mod in mods:
            total_mod_time += mod
        return total_mod_time

    def parse_rows(self, rows):
        for row in rows:
            yield self.parse_row(row)

    def parse_rows_for_today(self, rows, day):
        for row in reversed(rows):
            parsed_row = self.parse_row(row)
            if parsed_row[0].day != day:
                break
            yield parsed_row

    @staticmethod
    def parse_row(row):
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
            mod = timedelta(seconds=int(row[1]))
        except ValueError:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            mod = timedelta(minutes=int(row[1]))
        return date, mod

    def reset(self):
        FileUtils.add_file_if_it_does_not_exist(self.file_path)
        self.rows = []
