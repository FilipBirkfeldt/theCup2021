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


def log_inShareville(driver, userName, passWord):
    "Funktion som loggar in på sharewille"
    time.sleep(2)
    xpath = '//*[@id="search-results"]/li[2]/a'
    driver.find_element_by_xpath(xpath)
    print(driver.find_element_by_xpath(xpath).text)

    print('Log-in done')

def loopThroughList(driver): 
    time.sleep(2)
    element_list = driver.find_elements_by_class_name("sold-property-listing")
    data_list = []
    for element in element_list:
        data_list.append(element.text)

    print('done')
    return data_list