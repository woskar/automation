#! user/bin/env python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of eah line of text on the clipboard


# Project: Adding Bullets To Wiki Markup

# Description:
# A bullet is created by adding a star to each list element.
# This script copies text from the clipboard, adds a star and space
# at the beginning of each line and pastes this new text to the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Join lines together because pyperclip expects one string

text = '\n'.join(lines)
    
pyperclip.copy(text)



