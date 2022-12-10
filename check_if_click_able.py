from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, TimeoutException,ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time 

PATH = r"C:\Users\Hugo\PartyBot\chromedriver.exe"
driver = webdriver.Chrome(PATH)
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,ElementNotInteractableException, TimeoutException, ElementClickInterceptedException)
wait = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)
driver.get("https://www.pudelek.pl/robert-lewandowski-jednak-komentuje-30-milionow-premii-od-morawieckiego-to-sie-wszystko-dzieje-poza-pilkarzami-ktorzy-razem-z-kibicami-sa-ofiarami-6842487736318496a")

try:
    TermsAndConditions = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div/button[2]")))
    TermsAndConditions.click()
except NoSuchElementException:
    print("Terms and conditions not found")


# for i in range(30, 35):
#     try:
#         chk = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]/div[3]')))
#         ActionChains(driver).move_to_element(chk).double_click().perform()
#     except ignored_exceptions:
#         print('error')

# for i in range(30, 35):
#     try:
#         chk = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]/div[3]/div/div')))
#         ActionChains(driver).move_to_element(chk).perform()
#     except ignored_exceptions:
#         print("exception")


check = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[32]/div/div[2]/div[3]/div/div')
if check == "Następna strona":
        chk = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[32]/div/div[2]/div[3]/div/div')))
        possible_text = chk.get_attribute('innerHTML')
        ActionChains(driver).move_to_element(chk).click(chk).perform()
        ActionChains(driver).move_to_element(chk).click(chk).perform()
        print(possible_text)
else:
    print("the index has changed")
time.sleep(15)