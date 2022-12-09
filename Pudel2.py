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
            return "Comment is not on this page"
        


    def get_the_comment(self, text = None):
        if self.find_the_comment() != "Comment is not on this page" :
            Comment_to_like = self.like_comment()
        else:
            # Below I've pasted some examples of comment pages buttons. 
            # Unfotuantely there is not much to program and it seems we would need to pass a lot of conditionals 
            # if we would like to find the comment among others and iterate all of the pages. 
            # # //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[22]/div/div[3]/div[3]/div/div
            # //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[1]/div[1]/div/div/button
            # //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[31]/div/div[1]/div[3]/div/div/button
            # //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[27]/div/div[2]/div[3]/div/div/button
            # //*[@id="page_content"]/div[1]/div/div[3]/div/div/div/div/div[21]/div/div[2]/div[3]/div/div/button
            # Look for comment
        print("Looking for the comment page")
        

    # except NoSuchElementException:
    #     print("Article is not on this page")

    # def check_if_index_changed(self):
    #     comment_index = self.get_the_comment()


    def like_comment(self):
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