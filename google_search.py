import time
from datetime import datetime
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class MyChromeDriver:
    def __init__(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.sought_url = None

    def linkedin_sign_in(self):

        self.driver.get('https://www.linkedin.com/home')
        time.sleep(3)
        # Get_sign_in = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
        # Get_sign_in.click()

        Put_user = self.driver.find_element(By.ID, 'session_key')
        Put_user.send_keys('gagazor3@gmail.com')

        Put_password = self.driver.find_element(By.ID, 'session_password')
        Put_password.send_keys('Antiparasite3')

        Get_sign_in = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
        Get_sign_in.click()
        time.sleep(2)
        self.driver.get('https://www.linkedin.com/')

    def linkedin_sign_out(self):

        self.driver.get('https://www.linkedin.com/home')
        time.sleep(3)
        # Get_sign_in = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
        # Get_sign_in.click()

        Get_menu = self.driver.find_element(By.ID, 'ember25')
        Get_menu.click()
        time.sleep(2)
        Get_sign_out = self.driver.find_element(By.XPATH, '//*[@id="ember27"]/div/ul/li[3]/a')
        Get_sign_out.click()
        time.sleep(3)


    def go_to_linkedin(self, name="ARABI Mouhannad"):
        self.driver.get('http://www.google.be/')
        try:
        # identify element
            Get_cookies = self.driver.find_element(By.ID, 'L2AGLb')
            Get_cookies.click()

        # NoSuchElementException thrown if not present
        except NoSuchElementException:
            pass

        time.sleep(3)

        search_query = self.driver.find_element(By.NAME, 'q')

        search_query.send_keys('site:linkedin.com ' + name)
        Get_Search = self.driver.find_element(By.CLASS_NAME, 'gNO89b')
        Get_Search.submit()
        time.sleep(3)
        Get_first_request = WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'yuRUbf'))
        )
        get_url = self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div[1]/div/a')
        self.sought_url = get_url.get_attribute('href')
        Get_first_request.click()

    def go_to_linkedin_conditional(self, name="ARABI Mouhannad"):
        self.go_to_linkedin(name)
        sought_url_actual = self.sought_url
        print(re.findall(r"/in/(.*)", sought_url_actual))
        print(re.findall(r"/in/(.*)", self.driver.current_url))
        if (re.findall(r"/in/(.*)", sought_url_actual) != re.findall(r"/in/(.*)", self.driver.current_url)):
            self.linkedin_sign_in()
            time.sleep(2)
            self.linkedin_sign_out()
            self.go_to_linkedin(name)


    def get_soup(self):
        return BeautifulSoup(self.driver.page_source, 'html.parser')


if __name__ == '__main__':
    print('hello')

