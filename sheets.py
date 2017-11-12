''' script to download music sheets '''

import requests, os, bs4, threading
os.makedirs('noten', exist_ok=True)


import time, os, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = ''
location = ''

browser = webdriver.Firefox()
browser.get(url)

zettels = browser.find_elements_by_partial_link_text('Text')
print(zettels)

print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()
print('works checkpoint 1')
soup = bs4.BeautifulSoup(res.text, "lxml")


print('Done')