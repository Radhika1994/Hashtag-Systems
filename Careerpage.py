from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
class Assignmnet():
    def Careerpage(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
        driver.maximize_window()
        driver.find_element("name",'name').send_keys('Radhika')
        time.sleep(2)
        driver.find_element("name", 'email').send_keys('radhikareddy@gmail.com')
        time.sleep(2)
        driver.find_element("name", 'phone').send_keys('9491675694')
        time.sleep(2)
        driver.find_element("xpath", '//input[@id="inputFile"]').send_keys('C:/Users/Admin/Desktop/Radhika-QA--Resume.pdf')
        time.sleep(2)
        driver.find_element("xpath", '//textarea[@placeholder="Briefly Describe Yourself"]').send_keys('Testing')
        time.sleep(2)
        driver.find_element("xpath", '//button[normalize-space()="APPLY NOW"]').click()
        time.sleep(2)
findby = Assignmnet()
findby.Careerpage()
