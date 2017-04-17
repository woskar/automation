#! /usr/bin/env python3
# pw.py - An insecure password locker program

# Description:
# This script has to be run on the command line with one command line argument,
# which has to be the name of one of the accounts defined in a dictionary.The
# script then copies the password belonging to the account into the clipboard.

# Comments:
# the first line of this skript is the shebang line (Magic Line)
# which tells the computer where to find the python Interpreter
# save the file in the homefolder to access it from anywhere on the console
# when saved, make it executable by running chmod -x pw.py
# open with the command ./pw.py

#First create a dictionary that stores password for every account

PASSWORDS = {'email': 'blablabla',
             'blog': 'testpasswort123'}

# Commandline arguments will be stored in sys.argv
# command line argument is mandatory in our script,
# so we display a usage message if user forgot to give one

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line argument is the account name

# Given account name as command line argument, we copy the right password

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
