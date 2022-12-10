from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time 

PATH = r"C:\Users\Hugo\PartyBot\chromedriver.exe"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 10)

class Pudlowe_Love():

    def get_the_article(self, article_link):
        # Enter article
        driver.get(article_link)
        # Accept the terms
        try:
            TermsAndConditions = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div/button[2]")))
            TermsAndConditions.click()
        except NoSuchElementException:
            print("Terms and conditions not found")

    # try:
    def find_the_comment(self):
        # Call article opener
        self.get_the_article("https://www.pudelek.pl/robert-lewandowski-jednak-komentuje-30-milionow-premii-od-morawieckiego-to-sie-wszystko-dzieje-poza-pilkarzami-ktorzy-razem-z-kibicami-sa-ofiarami-6842487736318496a")
        # Comment content
        content_of_comment = "Lorem"
        # Mesure Time for looking 

        start_time = time.time()
        print("Trying to Loop through the first page")
        for i in range(0, 31):
            try:
                comment = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]')
                possible_text = comment.get_attribute('innerHTML')
                if content_of_comment in possible_text:
                    print(f"Found the article containing phrase. Index equals == {i}")
                    end_time = time.time()
                    total_time = end_time - start_time
                    print("Time of looking the comment is equal to: ", total_time) 
                    return i
            except NoSuchElementException:
                print(f"element not found, index: {i}")
        else:
            print("Not on this page")
            return False

    def find_the_comment_2(self):
            
            content_of_comment = "Lorem"
            # Mesure Time for looking 

            start_time = time.time()
            print("Trying to Loop through the first page")
            for i in range(0, 31):
                try:
                    comment = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{i}]/div/div[2]')
                    possible_text = comment.get_attribute('innerHTML')
                    if content_of_comment in possible_text:
                        print(f"Found the article containing phrase. Index equals == {i}")
                        end_time = time.time()
                        total_time = end_time - start_time
                        print("Time of looking the comment is equal to: ", total_time) 
                        return i
                except NoSuchElementException:
                    print(f"element not found, index: {i}")
            else:
                print("Not on this page")
                return False


    def get_the_comment(self, text = None):
        if self.find_the_comment() != False :
            Comment_to_like = self.like_comment()
            # Further part in case the comment is found on the x page.
        else:
            print("NEXT PAGE")
            #next_button = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]')
            # next_button = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]/div')
            # next_button = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]/div/div')
            # next_button = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]/div/svg')
            # next_button = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]/div/svg/path')
            # next_button = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]/div')
            # next_button = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]/div/div')
            # next_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[5]/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[2]/div[3]/div/div')
            next_button.click()
            print("Run the sec version of find comment")
            self.find_the_comment_2()


        # Solution to check the number of pages failed
        # else:
        #     print("Looking for the comment page")
        #     comment_pages = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[1]') 
        #     text_comment_pages = comment_pages.get_attribute('innerHTML')
        #     text_comment_pages = text_comment_pages.split()
        #     pages_buttons = [string for string in text_comment_pages if "</button></div></div></div>" in string]
        #     l_striped_buttons = [string.lstrip('type="button">') for string in pages_buttons]
        #     r_striped_buttons = [string.rstrip('</button></div></div></div>') for string in l_striped_buttons]
        #     print(f" buttons: {r_striped_buttons}")
        #     # read what's second page 
        #     next_page_button = driver.find_element(By.XPATH, '//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[1]/div[2]/div/div/button')
        #     read_next_page_button = next_page_button.get_attribute('innerHTML')
        #     if str(read_next_page_button) == r_striped_buttons[1]:
        #         print(f"Next page is {read_next_page_button}, and second element of el of final buttons is {r_striped_buttons[1]}", read_next_page_button==r_striped_buttons[1])
        #         #This doesnt work
        #         next_page_button.click()
        #         print("clicked button")
        #         self.find_the_comment()

    def like_comment(self):
        print("Liking the correct comment")
        pass
    #     print("Liking the comment starting now...")
    #     start_time = time.time()
    #     # comment_index = self.get_the_comment()
    #     # counter = driver.find_element(By.XPATH, f'//*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[{comment_index}]/div/div[1]/div[2]/div/button[1]/div/div')
    #     # counter_text = counter.get_attribute('innerHTML')

    #     while int(counter_text) < 150:

    #     end_time = time.time()
    #     total_time = end_time - start_time
    #     print("Time of liking the comment is equal to: ", total_time) 



pl = Pudlowe_Love()
pl.get_the_comment()