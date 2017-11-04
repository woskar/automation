''' script to download music sheets '''

import requests, os, bs4, threading
os.makedirs('noten', exist_ok=True)

