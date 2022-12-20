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

#pagina a ingresar(get = es cuando se accede al contenido de la propiedad)
Url = driver.get("https://es.investing.com/crypto/bitcoin")

#variable que guarda lo que encuentre el find_element, el find_element busca el div o elemento en la pagina

BTC = driver.find_element("xpath",'//*[@id="last_last"]')

#mensaje que avisa el precio del btc

print('El precio del bitcoin es de : '+ BTC.text)

#cierra la conexion con chrome

driver.quit()