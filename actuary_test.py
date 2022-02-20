import datetime
import unittest

from bs4 import BeautifulSoup
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from class_actuary import Actuary
from def_web_scrapping import Load_actuary
from google_search import MyChromeDriver

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        my_chrome_driver = MyChromeDriver()
        my_chrome_driver.go_to_linkedin()

        driver = my_chrome_driver.driver
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        student = Load_actuary(soup, driver.current_url)
        result = student.birthday_appr()


        self.assertNotEqual(result, '')

    def test_upper_2(self):
        student = Actuary()
        student.birthday_appr = datetime.datetime.now()
        student.now = datetime.datetime.now()
        result = student.get_birthday_appr()

        self.assertNotEqual(result, '')


if __name__ == '__main__':
    unittest.main()