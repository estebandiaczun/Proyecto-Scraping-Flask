import gspread
import time
from datetime import datetime
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#PATH = '../Scrapeo/chromedriver'
#driver = webdriver.Chrome(PATH)
#driver.get("https://www.google.com")

class ScrapearGMaps:
   
    data = {}
    worksheet = {}
    listas_almacenes = []
   
    def __init__(self):
        # Ruta de ChromeDriver
        # self.driver=webdriver.Chrome(executable_path='./chromedriver_win/chromedriver.exe')
        self.driver=webdriver.Firefox(executable_path='./geckodriver-v0.30.0-win64/geckodriver.exe')
        #self.driver = webdriver.Chrome(service=Service("./chromedriver_win32/chromedriver.exe"))
        #self.driver = webdriver.Chrome(executable_path="../Scrapeo/chromedriver")
       
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
   
    def scroll_the_page(self, i):
        try:
            # Gambiarra to load all places into the page
            # scrollable_div = self.driver.find_element_by_css_selector("div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc > div[aria-label*='Results for']")
            #section_loading = self.driver.find_element_by_class_name("section-loading")class="siAUzd-neVct section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc ecceSd"
            section_loading = self.driver.find_element(By.CLASS_NAME, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
            # self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # time.sleep(3)
            while True:
                actions = ActionChains(self.driver)
                actions.move_to_element(section_loading).perform()
                time.sleep(3)
                cant_1 = len(self.driver.find_elements(By.CLASS_NAME, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd"))
                cant = 1
                if i >= cant:
                #if i >= len(self.driver.find_elements(By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a')):
                    actions = ActionChains(self.driver)
                    actions.move_to_element(section_loading).perform()
                    time.sleep(3)
                    print("Entro al while y se quedo hay...")
                else:
                    break
        except:
            pass

    def get_geocoder(self, url_location): # gets geographical lat/long coordinates
        try:
            coords = re.search(r"!3d-?\d\d?\.\d{4,8}!4d-?\d\d?\.\d{4,8}",
                            url_location).group()
            coord = coords.split('!3d')[1]
            return tuple(coord.split('!4d'))
        except (TypeError, AttributeError):
            return ("", "")
       
    def get_name(self):
        try:
            return self.driver.find_element(By.XPATH, "//h1[contains(@class,'header-title')]").text
        except:
            return ""
       
    def get_address(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "[data-item-id='address']").text
        except:
            return ""
       
    def get_phone(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "[data-tooltip='Copiar el número de teléfono']").text
        except:
            return ""
       
    def get_website(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "[data-item-id='authority']").text
        except:
            return ""

   
    def scrape(self, url):
        try:
            self.driver.get(url)
           
            # element = self.driver.find_element(By.XPATH, "//button[.//span[text()='I agree']]")
            # element.click()
            listas_almacenes = []

            for i in range(0,20):
                self.scroll_the_page(i)

                place = self.driver.find_elements(By.CLASS_NAME, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")[i]
                #place = self.driver.find_element(By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a')[i]
                time.sleep(3)

                place.click()
                time.sleep(3)

                name = self.get_name()
                address = self.get_address()
                phone_number = self.get_phone()
                website = self.get_website()
                coords = self.get_geocoder(self.driver.current_url)

                listas_almacenes.append([name, address, phone_number, coords[0], coords[1], website])
                print(listas_almacenes)

                volver = self.driver.find_element(By.CLASS_NAME, "xoLGzf-icon")
                time.sleep(2)
                
                volver.click()
                time.sleep(3)
           
        except Exception as e:
            print(e)
       
        time.sleep(10)
        #self.driver.quit()

        return(self.data)
   
query = "exito bogotá"
url = "https://www.google.com/maps/search/"+query.replace(" ", "+")+"/"

gmaps = ScrapearGMaps()
print(gmaps.scrape(url))