import win32gui
import win32process
import time
import psutil


# time.sleep(2)
# active_process_id = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
# print(f"PID: {active_process_id}")
while True:
	print(win32gui.GetCursorPos())
	time.sleep(1)
# # Iterate over all running processes
# for proc in psutil.process_iter():
# 	# Get process detail as dictionary
# 	pInfoDict = proc.as_dict(attrs=['pid', 'name'])
# 	# Append dict of process detail in list
# 	try:
# 		if pInfoDict['pid'] in active_process_id:
# 			children = proc.children()
# 			print(children, pInfoDict['name'])
# 			for child in children:
# 				if child.pid in active_process_id:
# 					print(child.name())
# 					break
# 	except KeyError:
# 		pass

