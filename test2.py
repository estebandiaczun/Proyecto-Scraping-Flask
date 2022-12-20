#Importaciones de selenium y pandas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

driver = webdriver.Chrome(executable_path='/path/to/driver/chromedriver')
driver = webdriver.Chrome()
driver.get("https://www.google.com/")



