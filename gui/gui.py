#! usr/bin/env python3

'''
GUI Automation
Controlling the keyboard and the mouse

Prevent problems

log out: shuts down all running programs
window/linux: ctrl-alt-del
macOs: cmd-shifft-option-q

tell script to wait after every function call
pyautogui.PAUSE = 1.5 will make all pyAutoGui function calls wait 1.5sec

fail save feature
moving mouse cursor to upper-left corner of screen causes exception:
pyautogui.FailSaveException
handle with try/catch block
disable this with pyautogui.FAILSAVE = False

Controlling mouse movement:
coordinate system origin (0,0) is in upper-left corner
pyautogui.size() returns tuple with screen resolution (width, heigth)
pyautogui.moveTo(x, y, duration=0.5) moves mouse to (x,y) with dur default 0
pyautogui.moveRel(x, y, duration=1.5) relative movement x to right and y down
pyautogui.position() returns tuple of mouse cursor's position (x,y)


'''

import pyautogui
pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True
width, height = pyautogui.size() # store screen resolution

'''
# Move mouse on absolute path
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
'''

# Move mouse on relative path
for i in range(3):
    pyautogui.moveRel(100, 0, duration=0.1)
    pyautogui.moveRel(0, 100, duration=0.1)
    pyautogui.moveRel(-100, 0, duration=0.1)
    pyautogui.moveRel(0, -100, duration=0.1)
