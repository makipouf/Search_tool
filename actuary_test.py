import datetime
import unittest

from bs4 import BeautifulSoup

from class_actuary import Actuary
from def_web_scrapping import Load_actuary
from google_search import MyChromeDriver


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        my_chrome_driver = MyChromeDriver()
        my_chrome_driver.go_to_linkedin()

        driver = my_chrome_driver.driver
        soup = my_chrome_driver.get_soup()
        student = Load_actuary(soup, driver.current_url)
        result = student.birthday_appr()


        self.assertNotEqual(result, '')

    def test_upper_2(self):
        # Given
        student = Actuary()
        student.birthday_appr = datetime.datetime.now()
        student.now = datetime.datetime.now()

        # When
        result = student.get_birthday_appr()

        # Then
        self.assertEqual(result, '0 years')

    def test_upper_3(self):
        # Given
        student = Actuary()
        student.birthday_appr = datetime.datetime.now()
        student.now = datetime.datetime.now()

        # When
        result = student.get_birthday_appr()

        # Then
        self.assertEqual(result, '0 years')


if __name__ == '__main__':
    unittest.main()