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

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--disable-features=DefaultPassthroughCommandDecoder")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")

PATH = r"C:\Users\Hugo\PartyBot\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)


ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,ElementNotInteractableException, TimeoutException, ElementClickInterceptedException)
wait = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)
driver.get("https://www.pudelek.pl/robert-lewandowski-jednak-komentuje-30-milionow-premii-od-morawieckiego-to-sie-wszystko-dzieje-poza-pilkarzami-ktorzy-razem-z-kibicami-sa-ofiarami-6842487736318496a")
driver.maximize_window()

try:
    TermsAndConditions = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div/button[2]")))
    TermsAndConditions.click()
except NoSuchElementException:
    print("Terms and conditions not found")

comment_index = []
content_of_comment = "Lorem"

# Solution for the nextpage issue
def switch_to_next_page():
    time.sleep(3)
    for i in range(19, 36):
        for j in range(2,4):
            try:
                button = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[{j}]/div[3]/div/div')

                button_possible_text = button.get_attribute('innerHTML')
                print("checked")
                if "Następna" in button_possible_text:
                    driver.execute_script("arguments[0].click();", button)
                    print(f"clicked index_i: {i} and index_j: {j}", button_possible_text)
            except ignored_exceptions:
                pass

# def get_range_of_pages():
#     print("chaninging page")

#     for i in range(18, 36):
#         try:
#             number_of_pages = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]/div[2]/div/div/button')
#             possible_text = number_of_pages.get_attribute('innerHTML')
#             return possible_text
#         except ignored_exceptions:
#             print(f"index {i} is not clickable")


# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[11]/div/div[2]

def look_for_desired_comment_on_single_page():
    print("looking for comment")
    for i in range(0, 31):
        try:
            comment_xp = f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]'
            comment = driver.find_element(By.XPATH, comment_xp)
            possible_text = comment.get_attribute('innerHTML')
            if content_of_comment in possible_text:
                print(f"Found the article containing phrase. Index equals == {i}")
                comment_index.append(comment_xp)
        except ignored_exceptions:
            print(f"index: {i} doesn't contain the desired comment")
    if len(comment_index) == 0:
        switch_to_next_page()

def check_comment_index_list():
    while len(comment_index) == 0:
        look_for_desired_comment_on_single_page()
    return comment_index
    

# print(check_comment_index_list())

# Like button 
#
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[6]/div/div[1]/div[2]/div/button[1]/div/svg
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]



def likeing():
    our_comment_xpath = check_comment_index_list()[0]
    comment = driver.find_element(By.XPATH, our_comment_xpath)
    possible_text = comment.get_attribute('innerHTML')
    print(f" Found comment text {possible_text}")
    if content_of_comment in possible_text:
        like_button = our_comment_xpath[:-6]
        print(f" like button: {like_button}")
        new_like_button = like_button + "div[1]/div[2]/div/button[1]"
        # new_like_button_search = driver.find_element(By.XPATH, new_like_button)
        try:
            while content_of_comment in possible_text: 
                driver.execute_script("arguments[0].click();", new_like_button_search)
                driver.refresh()
        except ignored_exceptions:
            print("looking again")
            comment_index.pop()
            look_for_desired_comment_on_single_page()
    else: 
        look_for_desired_comment_on_single_page()

likeing()  



# second page : "next page"
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[26]/div/div[3]/div[3]/div/div
# third page 
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[22]/div/div[3]/div[3]/div/div
# number of pages 
# //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[34]/div/div[2]/div[2]/div/div/button

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


# check = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[32]/div/div[2]/div[3]/div/div')
# if check == "Następna strona":
#         chk = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[32]/div/div[2]/div[3]/div/div')))
#         possible_text = chk.get_attribute('innerHTML')
#         ActionChains(driver).move_to_element(chk).click(chk).perform()
#         ActionChains(driver).move_to_element(chk).click(chk).perform()
#         print(possible_text)
# else:
#     print("the index has changed")
# time.sleep(15)