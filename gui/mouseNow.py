#! usr/bin/env python3
# mouseNow.py - Displays the mouse cursor's current position.

'''
Project: Where is the mouse right now?

Being able to determine the mouse position is an important part of setting up
your GUI automation scripts. But it’s almost impossible to figure out the exact
coordinates of a pixel just by looking at the screen. It would be handy to have
a program that constantly displays the x- and y-coordinates of the mouse cursor
as you move it around.

At a high level, here’s what your program should do:

Display the current x- and y-coordinates of the mouse cursor.
Update these coordinates as the mouse moves around the screen.

This means your code will need to do the following:

Call the position() function to fetch the current coordinates.
Erase the previously printed coordinates by printing \b backspace characters to the screen.
Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.


'''

import pyautogui
print('Press Ctrl-C to quit.')

try:
    while True:
        # Get and print the mouse coordinates.
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        # \b erases the last printed character of the current line, doesn't go beyond \n
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
