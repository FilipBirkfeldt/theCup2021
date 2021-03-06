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
import stealData
import numpy as np

print('\n')
print('---------------------------------------------START AV SCRIPTET------------------------------------------------------------------')
print('\n')

def addPrisStegring(data_list): 
    cols=['Adress', 
        'Typ', 
        'Område',
        'Kvm/rum', 
        'Hyra',
        'Slutpris', 
        'DatumSåld',
        'Pris/Kvm', 
        'Mäklare']
    df_append = pd.DataFrame(columns=cols, data=[data_list])
    return df_append

def elva_cols(data_list): 
    columns=['Adress', 
            'Typ', 
            'Område',
            'Kvm/rum', 
            'Hyra',
            'Biarea',
            'Slutpris', 
            'DatumSåld',
            'Pris/Kvm', 
            'PrisStegring', 
            'Mäklare']
    df_append = pd.DataFrame(columns=cols, data=[data_list])
    return df_append

def createDataFrame(data_list): 

    df = pd.DataFrame()
    columns=['Adress', 
            'Typ', 
            'Område',
            'Kvm/rum', 
            'Hyra',
            'Slutpris', 
            'DatumSåld',
            'Pris/Kvm', 
            'PrisStegring', 
            'Mäklare']

    for i,data in enumerate(data_list):
        data = data.split('\n')
        if data is None: 
            continue

        if df.empty: 
            try: 
                df = pd.DataFrame(columns=columns, data=[data])
            except: 
                continue
        else:
            try:  
                if len(data) == 10: 
                    df_append = pd.DataFrame(columns=columns, data=[data])
                elif len(data) == 9:
                    df_append = addPrisStegring(data)
                elif len(data) == 11: 
                    df_append = elva_cols(data)

                df = df.append(df_append)
            except: 
                continue
    
    return df