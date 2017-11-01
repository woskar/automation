''' 
Using selenium to download exercise sheets from the web.
This script uses the selenium webbrowser and requests for the download.
October 2017
'''
import time, os, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://www.biostruct.uni-hd.de/Hohere_Analysis.php'
location = '/Users/Oskar/Dropbox/Ana3/'

browser = webdriver.Firefox()
browser.get(url)

zettels = browser.find_elements_by_partial_link_text('Übungsblatt')
print(zettels)

for i in range(len(zettels)):
    href = zettels[i].get_attribute('href')
    name = href.split('/')[-1]

    if os.path.isfile(location + name):
        print('File', name, 'already exisits at', location, '.')
        continue

    else:
        print('New File found, now saving...')
        
        res = requests.get(href)
        res.raise_for_status()

        zettelFile = open(os.path.join(location, name), 'wb')
        for chunk in res.iter_content(100000):
            zettelFile.write(chunk)
        zettelFile.close()
print('Quitting Browser')
time.sleep(2) 
browser.quit()
print('Done')

