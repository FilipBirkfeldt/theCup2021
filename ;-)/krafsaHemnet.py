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

def krafsa(driver): 
    time.sleep(2)

    kvm_list = []
    kvm_pris_list = []
    adress_list = []
    slutpris_list = []
    diff_list = []
    datum_list = []
    hyra_list = []
    #maklare_list = []

    n = 0 

    while n <= 4:
        elements_adress = driver.find_elements_by_class_name("item-result-meta-attribute-is-bold")
        for element in elements_adress:
            adress_list.append(element.text)

        elements_hyra = driver.find_elements_by_class_name("sold-property-listing__fee")
        for element in elements_hyra:
            hyra_list.append(element.text)

        elements_kvm = driver.find_elements_by_class_name("sold-property-listing__subheading")
        i = 2
        for element in elements_kvm:
            if (i%2) == 0:  
                kvm_list.append(element.text)
            else: 
                slutpris_list.append(element.text)
            i+=1

        elements_kvm_pris = driver.find_elements_by_class_name("sold-property-listing__price-per-m2")
        for element in elements_kvm_pris:
            kvm_pris_list.append(element.text)

        elements_datum = driver.find_elements_by_class_name("sold-property-listing__sold-date")
        for element in elements_datum:
            datum_list.append(element.text)

        elements_diff = driver.find_elements_by_class_name("sold-property-listing__price-change")
        for element in elements_diff:
            diff_list.append(element.text)

        element_next = driver.find_element_by_class_name("next_page")
        element_next.send_keys(Keys.RETURN)
        n+=1

    driver.close()

    print('done')
    return adress_list, hyra_list, kvm_list, kvm_pris_list, datum_list, slutpris_list, diff_list