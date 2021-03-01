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

def pyssla(data):
    #df = pd.DataFrame(data)

    df = pd.DataFrame(data)

    #headers = ['gata','typ','område','kvm','hyra','slutpris','datum','kvm_pris','ökning','mäklare']
    #df.columns = headers

    return df

a =[1,2,3,4]
