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