#! python3

'''
Automatisches Einschalten von Sonosboxen
'''


import pyautogui
pyautogui.FAILSAFE = True
print('Press Ctrl-C or move mouse to upper left corner to quit.')

# store screen resolution
width, height = pyautogui.size()
print('Screen resolution is width', width, ', height', height)

# Bewege Position auf bestimmte Position
pyautogui.moveTo(100, 100, duration=0.25)

pyautogui.rightClick()
pyautogui.doubleClick()