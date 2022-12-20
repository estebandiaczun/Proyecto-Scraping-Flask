#Importaciones de selenium y pandas
#la clase keys importa el uso de las teclas especiales del teclado como ALT etc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

#Declara de donde sale el path 

PATH = "home/ediaczun/python3/ chromedriver.exe"

#declara el navegador

driver = webdriver.Chrome(PATH)

#(para que yo ingrese la pagina) val = input('Ingrese una pagina porfa: ')
#pagina a ingresar 
Url = driver.get("https://es.investing.com/crypto/ethereum")

#variable que guarda lo que encuentre el find_element, el find_element busca el div o elemento en la pagina

ETH = driver.find_element("xpath",'//*[@id="last_last"]')

#mensaje que avisa el precio del btc

print('El precio del ethereum es de : '+ ETH.text)

#cierra la web
driver.quit()
