from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

PATH = r"C:\Users\Hugo\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://party.pl/newsy/plebiscyt-na-15-lecie-party-wybierz-z-nami-ikone-stylu-glosuj-972-r28/?fbclid=IwAR3E3D9gs6UGQ32kEyYzI4fkRKsGHysG1Q0KBaYgJ2wEXQ34rTXqKCBJxbI")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

button = driver.find_element_by_xpath("//*[@id='tcf277-permissions-modal']/div[3]/div/button[2]")
button.click()
# button = driver.find_element_by_class_name("tcf277-button--slim")
# button.click()
print("check")