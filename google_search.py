import time
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


class MyChromeDriver:
    def __init__(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)

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

        self.driver.get('https://www.linkedin.com/')


    def go_to_linkedin(self, name="ARABI Mouhannad"):
        self.driver.get('http://www.google.be/')
        try:
        # identify element
            Get_cookies = self.driver.find_element(By.ID, 'L2AGLb')
            Get_cookies.click()

        # NoSuchElementException thrown if not present
        except NoSuchElementException:
            print("Accepting cookies is not needed")

        time.sleep(3)

        # Get_English = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/a[2]')
        # Get_English.click()
        # time.sleep(3)
        # locate search form by_name

        search_query = self.driver.find_element(By.NAME, 'q')

        search_query.send_keys('site:linkedin.com ' + name)
        Get_Search = self.driver.find_element(By.CLASS_NAME, 'gNO89b')
        Get_Search.submit()
        time.sleep(3)

        Get_first_request = self.driver.find_element(By.CLASS_NAME, 'yuRUbf')
        Get_first_request.click()

    def get_soup(self):
        return BeautifulSoup(self.driver.page_source, 'html.parser')


if __name__ == '__main__':
    print('hello')

