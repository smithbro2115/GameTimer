from Utils.FileUtils import resource_path
from Utils.CachingUtils import read_from_config, add_to_config
from configparser import NoSectionError, NoOptionError
from datetime import datetime
import pygame
pygame.mixer.init(48000)


class NotificationManager:
    def __init__(self, parent):
        self.parent = parent
        self.time_since_last_warning_tone = None
        self.time_since_last_alarm_tone = None

    def reset(self):
        self.time_since_last_warning_tone = None
        self.time_since_last_alarm_tone = None
        pygame.mixer.music.stop()

    @staticmethod
    def get_time_between_alarms():
        try:
            return int(read_from_config("SETTINGS", "time_between_alarms"))
        except (NoOptionError, NoSectionError):
            add_to_config("SETTINGS", "time_between_alarms", 60)
            return 60

    def user_conditions(self, user):
        return user == self.parent.current_user and user.user_clock.state

    def check_warning(self, user):
        if self.user_conditions(user):
            if self.time_since_last_warning_tone is None:
                play_warning_tone()
                self.time_since_last_warning_tone = datetime.now()

    def check_alarm(self, user):
        if self.user_conditions(user):
            if self.time_since_last_alarm_tone is None:
                play_alarm_tone()
                self.time_since_last_alarm_tone = datetime.now()
            elif (datetime.now() - self.time_since_last_alarm_tone).total_seconds() > self.get_time_between_alarms():
                play_alarm_tone(1)
                self.time_since_last_alarm_tone = datetime.now()


def play_warning_tone(loops=2):
    pygame.mixer.music.load(resource_path("Sounds\\warning.mp3"))
    pygame.mixer.music.play(loops)


def play_alarm_tone(loops=2):
    pygame.mixer.music.load(resource_path("Sounds\\alarm.mp3"))
    pygame.mixer.music.play(loops)
