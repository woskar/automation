#! usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
'''
python project mcb
Multi-Clip-Board

Say you have the boring task of filling out many forms in a web page
or software with several text fields. The clipboard saves you from
typing the same text over and over again. But only one thing can be
on the clipboard at a time. If you have several different pieces of
text that you need to copy and paste, you have to keep highlighting
and copying the same few things over and over again.

You can write a Python program to keep track of multiple pieces of
text. This “multiclipboard” will be named mcb.pyw (since “mcb” is
shorter to type than “multiclipboard”). The .pyw extension means that
Python won’t show a Terminal window when it runs this program.
(See Appendix B for more details.)

The program will save each piece of clipboard text under a keyword.
For example, when you run py mcb.pyw save spam, the current contents
of the clipboard will be saved with the keyword spam. This text can
later be loaded to the clipboard again by running py mcb.pyw spam.
And if the user forgets what keywords they have, they can run py
mcb.pyw list to copy a list of all keywords to the clipboard.

Here’s what the program does:

The command line argument for the keyword is checked.
If the argument is save, then the clipboard contents are saved to the keyword.
If the argument is list, then all the keywords are copied to the clipboard.
Otherwise, the text for the keyword is copied to the clipboard.

This means the code will need to do the following:

Read the command line arguments from sys.argv.
Read and write to the clipboard.
Save and load to a shelf file.

'''

import shelve # save new piece of cliboard text to a shelf file
import pyperclip # copying and pasting
import sys # reading the command line arguments

mcbShelf = shelve.open('mcb') # create shelf file with the prefix mcb

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# first arg: name of program
# second arg: save or other keyword
# third arg: what to save

elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
  

mcbShelf.close()
