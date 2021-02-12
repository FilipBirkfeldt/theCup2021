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

def collect_ads():
    for i in range(1, 31):
        # x_path = '//*[@id="MainCol"]/div[1]/ul/li[i]'
        i = str(i)
        x_path='//*[@id="MainCol"]/div[1]/ul/li['+(i)+(']')
        company_name = driver.find_element_by_xpath(x_path)
        job_info = company_name.text
        job_v1 = [job_info]
        job_v1 = job_v1[0].split('\n')
        job_vector.append(job_v1)


# Funktion som tar fram hur många kolumner som behövs i DataFrame: 
def col_nbr(lst):
    maxList = max(lst, key=lambda i:len(i))
    maxLength = len(maxList)
    return maxLength


def create_dataframe(list): 
    if number_of_cols == 5:
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    elif number_of_cols==6: 
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch', 'fill_out_1']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    elif number_of_cols==7: 
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch', 'fill_out_1', 'fill_out_2']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    else: 
        print('fel i create_dataframe... ')
    return df_jobb