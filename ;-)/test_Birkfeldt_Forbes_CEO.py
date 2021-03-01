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
import talkWithHemnet

from selenium.webdriver.common.keys import Keys

#import sorteraMig

print('''
 \n
---------------------------------------------START AV SCRIPTET------------------------------------------------------------------
\n
''')

url = 'https://www.hemnet.se/salda/bostader?housing_form_groups%5B%5D=apartments&living_area_max=40&location_ids%5B%5D=898741&selling_price_max=4000000'
 
# Skapar driver-objekt samt beautiful.Soup - objekt 
driver=webdriver.Chrome('/Applications/chromedriver') #navigate to page
driver.get(url)

data_list = talkWithHemnet.loopThroughList(driver)
[print(data) for data in data_list]
 
#df = pysslaHemnet.pyssla(data_list) 
#print(df)