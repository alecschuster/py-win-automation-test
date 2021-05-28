import pyautogui
import time
import subprocess

screenWidthCheck, screenHeightCheck = 2560, 1440

screenWidth, screenHeight = pyautogui.size()

if (screenWidthCheck != screenWidth) or (screenHeightCheck != screenHeight):
  print('error: please edit vals of width/height in source code test.py')
  exit()
else:
  print('Checks passed')

  print(screenWidth, screenHeight)

subprocess.Popen("C:\\Program Files (x86)\\GPU-Z\\GPU-Z.exe")
# pyautogui.doubleClick(2440,599)

time.sleep(2)


pyautogui.click(1298,386)

pyautogui.doubleClick(1241,420)

pyautogui.typewrite("Cave Johnson")

pyautogui.click(1185,453)

pyautogui.typewrite("optional@email.com")

pyautogui.click(1177,487)

pyautogui.typewrite("Automation with Python! I will now press close in 2 seconds")

time.sleep(2)

pyautogui.click(1438,811)

