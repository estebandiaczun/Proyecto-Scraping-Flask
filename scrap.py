#Importaciones de selenium y pandas
#la clase keys importa el uso de las teclas especiales del teclado como ALT, esc etc
from time import sleep
from datetime import date
import pandas as pd
import json
from datetime import datetime
import os
import shutil
from pathlib import Path 
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#Declara de donde sale el path 
PATH = "/ediaczun/escritorio/python3/Proyecto-Scraping-Flask"

#declara el navegador
driver = webdriver.Chrome(ChromeDriverManager().install())

#pagina a ingresar
Url = driver.get("https://www.coingecko.com/es")


#variables que guardan lo que encuentre el find_element, el find_element busca el div o elemento en la pagina
BTC = driver.find_element("xpath",'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[1]/td[4]/div/div[2]/span')

ETH = driver.find_element("xpath",'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[2]/td[4]/div/div[2]/span')

USDT = driver.find_element("xpath",'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[3]/td[4]/div/div[2]/span')

USDC = driver.find_element("xpath",'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[4]/td[4]/div/div[2]/span')

BNB = driver.find_element("xpath",'/html/body/div[4]/div[4]/div[6]/div[1]/div/table/tbody/tr[5]/td[4]/div/div[2]/span')


#variables que guardan el precio
msj1 = ('Bitcoin: '+ BTC.text )
msj2 = ('Ethereum: '+ ETH.text )
msj3 = ('USDT: '+ USDT.text )
msj4 = ('USDC: '+ USDC.text )
msj5 = ('BNB: '+ BNB.text )

tabla = [msj1 + msj2 + msj3 + msj4 + msj5]

table = " ".join(tabla)

#Intente colocarle la fecha al archivo
'''
now = datetime.now()
date = now.strftime("%m/%d/ %H:%M:%S")
'''

#crea el archivo precios, si ya hay uno lo sobreescribe 
file = open("precios.txt" ,"w")

file.write(table)
    
file.close()


#cierra la web
driver.quit() 

'''
1) estudiate esto y create el repo.
2) subi lo que tengas hecho de flask
3) estudiate lo de fastAPI
4) create la documentación modelo de una API
5) subila a Github
'''


