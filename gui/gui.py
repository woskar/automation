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
pyautogui.click() virtual mouse click default: left click at current position
optional arguments :(x, y, button='left'/'middle'/'right')
click is composed of the following two functions, which take same arguments
pyautogui.mouseDown() pushes mouse button down
pyautogui.mouseUp() releases the mouse button
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.doubleClick() performs two Clicks with left button
dragging: moving mouse while holding down one button
pyautogui.dragTo() absolute dragging, pass duration keyword for proper action
pyautogui.dragRel() relative dragging
pyautogui.scroll(amount) scrolls up if positive, down if negative

Checking visual information:
im = pyautogui.screenshot() # takes a screenshot and saves it as im
im.getpixel((0,0)) # returns tripel with (R,G,B) color of the pixel
### error?! ### mac returns four values with getpixel (maybe opacity) raises exception
pixelMatchesColor() # returns true if pixel at x,y on screen matches color

# find part of screenshot on screen, didn't work for me, did not return the right coordinates
pyautogui.locateOnScreen('picture.png') returns coordinates of picture on screen
returns (x, y, widht, height) xy being coordinates of edges, none if not found
pass the four-tuple to center mehtod to get pixel to click on:
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('submit.png')))

pyautogui.locateAllOnScreen() can find image in several places
retruns Generator Object, can be passed to list() to return list of four-int-tuples

Control the keyboard:
# note: uses english (QWERTY) keyboard
first send a mouse click to the text filed to ensure it has focus
pyautogui.typewrite('text', 0.2) sends virtual keypresses to the computer, 0.2sec pause between each
Special keys: 'esc', 'enter'/'return'/'\n', 'left', 'up', 'right'
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y']) # pass keys to press individually in list
pyautogui.keyDown()
pyautogui.keyUp()
pyautogui.press() #bundles the down and up functions
for $ run: pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c') # presses ctrl and c and releases them in the reverse order

# List all keys with
pyautogui.KEYBOARD_KEYS
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']




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
'''
# Move mouse on relative path
for i in range(3):
    pyautogui.moveRel(100, 0, duration=0.1)
    pyautogui.moveRel(0, 100, duration=0.1)
    pyautogui.moveRel(-100, 0, duration=0.1)
    pyautogui.moveRel(0, -100, duration=0.1)
'''

pyautogui.hotkey('shift', '4')


pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

pyautogui.size()
