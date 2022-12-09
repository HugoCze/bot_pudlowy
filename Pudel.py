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
# driver.maximize_window() # For maximizing window
# driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
# Accept the terms - in order to proceed further to the site ->
button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div/button[2]")
# /html/body/div[3]/div/div[2]/div[3]/div/button[2]
button.click()

def find_comment():
    print("searching for comment")
    for i in range(0, 31):
        try:
            comment = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]')
                                                    # //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[16]/div/div[1]/div[2]/div/button[1]
            possible_text = comment.get_attribute('innerHTML')
            # print(possible_text)
            if "Lorem" in possible_text:
               return i
        except NoSuchElementException:
            print(f"element not found, index: {i}")
        
        

def like_comment(index):
    # counter = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[12]/div/div[1]/div[2]/div/button[1]/div/div')
    # counter = counter.get_attribute('innerHTML')
    print("liking")
    counter = 0
    start_time = time.time()
    while int(counter) < 100:
        # try:
        button = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{index}]/div/div[1]/div[2]/div/button[1]')))
    # button = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{index}]/div/div[1]/div[2]/div/button[1]')
    # button = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{index}]/div/div[1]/div[2]/div/button[1]/div')
        button.click()
        print("click")
        counter += 1
        #     comment = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{index}]/div/div[2]')
        #     possible_text = comment.get_attribute('innerHTML')
        # except "Lorem" not in possible_text:
        #     find_comment()
            
        counter = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{index}]/div/div[1]/div[2]/div/button[1]/div/div')
        counter = counter.get_attribute('innerHTML')
    end_time = time.time()
    total_time = end_time - start_time
    print("Time: ", total_time) 

like_comment(find_comment())
# Next stage search through the comments to find the one we are actually would like to 'like'...
# Most "TOP" comment:                       xpath: //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[3] -> class="sc-1mskw74-0 iBRgdS"
# Random comment below made 3 minutes ago:  xpath: /html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[15] -> class="sc-1mskw74-0 iBRgdS"
# Last comment on the first comment page:   xpath: //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[30]
# Random comment from the second page       xpath: /html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[11]
# Unfortunately these are not depend from the last value 
# https://www.pudelek.pl/robert-lewandowski-jednak-komentuje-30-milionow-premii-od-morawieckiego-to-sie-wszystko-dzieje-poza-pilkarzami-ktorzy-razem-z-kibicami-sa-ofiarami-6842487736318496a
# Link is also not different than previously ... 

# comment = driver.find_element_by_xpath("/html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[3]")
# comment = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[3]')
# possible_text = comment.get_attribute('innerHTML')
# # stripped = possible_text.strip()
# # print(stripped)
# if 'Reprezentacja' in possible_text:
#     print("Znalezione!")
# else:
#     print("Pudlo")
# try:
#     This_Page = None
# def find_comment():
#     for i in range(5, 31):
#         comment = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]')
#         if not NoSuchElementException:
#             print(comment)
#             possible_text = comment.get_attribute('innerHTML')
#             if "Lorem" in possible_text:
#                 print(f"comment: {comment}, i: {i}, possible text: {possible_text}")
# try:
#     find_comment()
# except NoSuchElementException:
#     find_comment() 
#     else:
#         This_Page = False
# except This_Page == False:
    

# /html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[3]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[3]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[20]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[3]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[20]
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[20]/div/div[2]
#//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]/div/div
