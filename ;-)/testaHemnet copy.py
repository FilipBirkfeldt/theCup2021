#import pandas as pd
#df = []
#df = pd.DataFrame()

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

import krafsaHemnet

df = pd.read_csv('/Users/sebastianbalsom/git/theCup2021/;-)/hemnet.csv')
headers = ['sjas','Adress','Hyra','Storlek','Pris per kvm','Försäljningsdatum','Slutpris','Diff']
df.columns = headers
del df['sjas']
df['Hyra'] = df['Hyra'].str.replace(r'\D','')
df['Slutpris'] = df['Slutpris'].str.replace(r'\D','')
df['Pris per kvm'] = df['Pris per kvm'].str.replace(r'\D','')
df['Försäljningsdatum'] = df['Försäljningsdatum'].str.replace('Såld ','')
df['Storlek'] = df['Storlek'].str.replace('m²','')
df['Storlek'] = df['Storlek'].str.replace('rum','')
df[['kvm','rum']] = df['Storlek'].str.split(' ',1, expand=True)
del df['Storlek']

print(df) 

print(df.dtypes)