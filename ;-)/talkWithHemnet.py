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
import time

from selenium.webdriver.common.keys import Keys

def loopThroughList(driver): 
    time.sleep(2)

    data_list = []
    n = 0 

    while n <= 4:
        element_list = driver.find_elements_by_class_name("sold-property-listing")
        for element in element_list:
            data_list.append(element.text)

        element_next = driver.find_element_by_class_name("next_page")
        element_next.send_keys(Keys.RETURN)
        n+=1

    driver.close()

    print('done')
    return data_list
