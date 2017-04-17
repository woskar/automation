"""
# Reading and Writing files

Folder names and filenames are not case sensitive on
Windows and macOS but they are on Linux.

Windows: root C:\ and backslashes \ as separators
Linux and Mac: root /. and forwardslashes / as separators
use os.path.join() function (import os)
os.path.sep returns the separator used on the operating system

Current working directory (cwd): os.getcwd()
change cwd with: os.chdir('new path')

. for this directory
.. for the parent directory

./ at the start of a relative path is optional:
./spam.txt and spam.txt are the same.

create new directories: os.makedirs('new path')
pass e.g. /delicious/waffles to create two new folders

os.path.abspath(pathname) returns string of the path of pathname
os.path.isabs(pathname) returns true if path is absolute

os.path.relpath(path, start) returns string of a relative path from the start to path,
if start is not provided, then current working directory is used as start path

os.path.dirname(path) returns string of everything before the last / in path
os.path.basename(path) returns string of everything after last / in path
so path is composed of dirname/basename, basename is filename
os.path.split(path_to_file) returns tuple of (dirname, basename)
to split at every / use pathname.split(os.path.sep)

os.path.getsize(pathname) returns size of file in pathname in bytes
os.listdir(pathname) returns list of filename strings for each file in pathname

combine the two to get the total size in a path (here cwd):
totalSize = 0
for filename in os.listdir('.'):
    totalSize = totalSize + os.path.getsize(filename)

# check path validity
os.path.exists(path) returns true if path exists
os.path.isfile(path) returns true if path argument exists and is a file
os.path.isdir(path) returns true if path argument exists and is a folder
use for example to check if a hard drive is connected

# reading/writing
following functions applicable to plaintext files
which contain only basic text characters like .txt or .py files
other files are binary files, pdfs, images, executables etc

Three steps of reading or writing:
1. call open(path, 'r') to return a file object (in reading 'r' plaintext mode (default) or write 'w' or append 'a') if path does not exist yet, file will be created
2. call read() method on file object, returns one string with all the text, or write(), pass a string with the text to write, or readlines(), returns list of strings with lines, newline characters \n have to be added manually
3. close file by calling close() on the file object

# shelve module
allows to save variables/data from python programs to binary shelf files for later re-load
import shelve
shelfFile = shelve.open('mydata') # create shlef object for writing ('w' not needed with shelve)
cats = ['Zophie', 'Pooka', 'Simon'] # an example variable
shelfFile['cats'] = cats # make changes to shelf file as if it was a dictionary
shelfFile.close() # close the file when you're done
# running this will create a mydata.db file
openShelfFile = shelve.open('mydata') # open file for reading
openShelfFile['cats'] # retrieve data saved with key cats
list(openShelfFile.values()) # get list of stored values (cast to get true list and not list-like values)
list(openShelfFile.keys())
openShelfFile.close() # close file again

use pretty printing to save variables in correct formatted form
saving the code to a .py file lets you import the data like a normal module
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats) # optional, returns a formatted string with cats-dictionary
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

# now our file is a .py module and can be imported like any other module
import myCats # import
myCat.cats # returns the stored data
myCat.cats[0] # returns first element in list

benefit of a .py file:
is text file, can be read and modified with any simple editor
only for basic data types like integers, floats, strings, lists, dictionaries

for most applications, shelve module preferred
file objects cannot be encoded as text

"""
