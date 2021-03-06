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
import numpy as np

import stealData
import cleanData

print('\n')
print('---------------------------------------------START AV SCRIPTET------------------------------------------------------------------')
print('\n')

url = 'https://www.shareville.se/me/feed/trades'
url = 'https://www.hemnet.se/salda/bostader?location_ids%5B%5D=898741&item_types%5B%5D=bostadsratt&rooms_max=2.5&selling_price_max=4500000'
# Skapar driver-objekt samt beautiful.Soup - objekt 
driver=webdriver.Chrome('/Applications/chromedriver')
driver.get(url)


data_list = stealData.krafsa(driver)
df = cleanData.createDataFrame(data_list)
df.to_excel('Data/hemnetData.xlsx', index=False)
