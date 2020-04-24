import win32gui
import win32process
import time
import psutil
import threading


GAMES = ["javaw.exe", "robloxplayerbeta.exe", "civilizationv_dx11.exe"]

time.sleep(2)


def get_current_processes() -> dict:
	processes_dict = {}
	for proc in psutil.process_iter():
		pInfoDict = proc.as_dict(attrs=['pid', 'name'])
		processes_dict[pInfoDict['pid']] = pInfoDict['name']
	return processes_dict


def get_current_process_name() -> str:
	active_process_id = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]
	current_processes = get_current_processes()
	return current_processes[active_process_id]


def is_playing_game():
	try:
		return get_current_process_name().lower() in GAMES
	except KeyError:
		return False


class Reminder:
	def __init__(self, remind, minutes_to_check=5):
		self.timer = Timer()
		self.timer.interval = minutes_to_check*60
		self.timer.callback = self.run_check
		self.callback = remind

	def start(self):
		self.timer.start()

	def run_check(self):
		if is_playing_game():
			self.callback()


class Timer(threading.Thread):
	def __init__(self):
		super(Timer, self).__init__()
		self.interval = 0
		self.callback = None
		self.canceled = False
		self.setDaemon(True)

	def run(self):
		while not self.canceled:
			time.sleep(self.interval)
			self.callback()
