from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time 
from selenium.webdriver.common.by import By

PATH = r"C:\Users\Hugo\PartyBot\chromedriver.exe"

driver = webdriver.Chrome(PATH)

article_link = "https://www.pudelek.pl/robert-lewandowski-jednak-komentuje-30-milionow-premii-od-morawieckiego-to-sie-wszystko-dzieje-poza-pilkarzami-ktorzy-razem-z-kibicami-sa-ofiarami-6842487736318496a"

driver.get(article_link)
wait = WebDriverWait(driver, 10)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
# Accept the terms - in order to proceed further to the site ->
button = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div/button[2]")
# /html/body/div[3]/div/div[2]/div[3]/div/button[2]
button.click()

# Next stage search through the comments to find the one we are actually would like to 'like'...
# Most "TOP" comment:                       xpath: //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[3] -> class="sc-1mskw74-0 iBRgdS"
# Random comment below made 3 minutes ago:  xpath: /html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[15] -> class="sc-1mskw74-0 iBRgdS"
# Last comment on the first comment page:   xpath: //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[30]
# Random comment from the second page       xpath: /html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[11]
# Unfortunately these are not depend from the last value 
# https://www.pudelek.pl/robert-lewandowski-jednak-komentuje-30-milionow-premii-od-morawieckiego-to-sie-wszystko-dzieje-poza-pilkarzami-ktorzy-razem-z-kibicami-sa-ofiarami-6842487736318496a
# Link is also not different than previously ... 

# comment = driver.find_element_by_xpath("/html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[3]")
comment = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[3]')
possible_text = comment.get_attribute('innerHTML')
# stripped = possible_text.strip()
# print(stripped)
if 'Reprezentacja' in possible_text:
    print("Znalezione!")

# 
# /html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[3]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[3]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[20]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[3]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[20]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[20]/div/div[2]