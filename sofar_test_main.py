# yesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyes
# Main class for Filips Web-scraping tool :) 

# https://github.com/FilipBirkfeldt/job_search
# command+shift+P 

# Test är du där eller
# hmm 

import time 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import numpy as np
import requests, bs4

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import talkWithShareville

print('\n')
print('---------------------------------------------START AV SCRIPTET------------------------------------------------------------------')
print('\n')

url = 'https://www.shareville.se/me/feed/trades'
url = 'https://www.hemnet.se/salda/bostader?location_ids%5B%5D=18031&item_types%5B%5D=bostadsratt&sold_age=12m'
# Skapar driver-objekt samt beautiful.Soup - objekt 
driver=webdriver.Chrome('/Applications/chromedriver')
driver.get(url)

data_list = talkWithShareville.loopThroughList(driver)
[print(data) for data in data_list]
