from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time 

while 1==1:
    try:
        PATH = r"C:\Users\Hugo\PartyBot\chromedriver.exe"

        driver = webdriver.Chrome(PATH)
        link = "https://party.pl/newsy/plebiscyt-na-15-lecie-party-wybierz-z-nami-ikone-stylu-glosuj-972-r28/?fbclid=IwAR3E3D9gs6UGQ32kEyYzI4fkRKsGHysG1Q0KBaYgJ2wEXQ34rTXqKCBJxbI"
        
    
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        driver.maximize_window() # For maximizing window
        driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
        button = driver.find_element_by_xpath("//*[@id='tcf277-permissions-modal']/div[3]/div/button[2]")
        button.click()
    
        driver.maximize_window() # For maximizing window
        driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
        second_place = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/label/div/div[2]")
        second_place_content = second_place.get_attribute('innerHTML')
        second_place_striped = second_place_content.strip()
        if second_place_striped == "Kinga Rusin":
            element = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/label/div/div[1]")
        else:
            element = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[3]/div/label/div/div[1]")

        element.click()
        print("check2")
        driver.switch_to.window(driver.window_handles[0])
        driver.delete_all_cookies()
    except NoSuchElementException:
        driver.maximize_window() # For maximizing window
        driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

        second_place = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/label/div/div[2]")
        second_place_content = second_place.get_attribute('innerHTML')
        second_place_striped = second_place_content.strip()
        if second_place_striped == "Kinga Rusin":
            element = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/label/div/div[1]")
        else:
            element = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[3]/div/label/div/div[1]")

        element.click()
        print("check2")
        driver.switch_to.window(driver.window_handles[0])
        driver.delete_all_cookies()

print("done")