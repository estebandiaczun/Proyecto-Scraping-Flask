#Imports Selenium & Pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import time
from datetime import datetime
import re


class ScrapearGmaps:
    
    data = {}
    worksheet = {}
    listas_abogados = ()
    
    def __init__(self):
        driver = webdriver.Chrome(PATH)
        PATH = "home/ediaczun/python3/ chromedriver.exe"
        Url = driver.get("https://es.investing.com/crypto/ethereum")
        
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        pass