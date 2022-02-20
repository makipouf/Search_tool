import time
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyChromeDriver:
    def __init__(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)


    def go_to_linkedin(self):
        self.driver.get('http://www.google.be/')
        Get_cookies = self.driver.find_element(By.ID, 'L2AGLb')
        Get_cookies.click()
        time.sleep(3)

        Get_English = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/a[2]')
        Get_English.click()
        time.sleep(3)
        # locate search form by_name

        search_query = self.driver.find_element(By.NAME, 'q')
        # send_keys() to simulate the search text key strokes
        # search_query.send_keys('site:linkedin.com "Gaétan Gellens"')
        # search_query.send_keys('site:linkedin.com "Rubin Daija"')
        # search_query.send_keys('site:linkedin.com "Meghna Lakshminarayanan"')
        search_query.send_keys('site:linkedin.com "ARABI Mouhannad"')
        Get_Search = self.driver.find_element(By.CLASS_NAME, 'gNO89b')
        Get_Search.submit()
        time.sleep(3)

        Get_first_request = self.driver.find_element(By.CLASS_NAME, 'yuRUbf')
        Get_first_request.click()


if __name__ == '__main__':

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get('http://www.google.be/')
    Get_cookies = driver.find_element(By.ID, 'L2AGLb')
    Get_cookies.click()

    Get_English = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/a[2]')
    Get_English.click()

    # locate search form by_name

    search_query = driver.find_element(By.NAME, 'q')
    # send_keys() to simulate the search text key strokes
    # search_query.send_keys('site:linkedin.com "Gaétan Gellens"')
    # search_query.send_keys('site:linkedin.com "Rubin Daija"')
    # search_query.send_keys('site:linkedin.com "Meghna Lakshminarayanan"')
    search_query.send_keys('site:linkedin.com "ARABI Mouhannad"')
    Get_Search = driver.find_element(By.CLASS_NAME, 'gNO89b')
    Get_Search.submit()

    Get_first_request = driver.find_element(By.CLASS_NAME, 'yuRUbf')
    Get_first_request.click()

    driver.back()

    Get_first_request = driver.find_element(By.CLASS_NAME, 'yuRUbf')
    Get_first_request.click()

    # Mouhannad Arabi

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    print(soup.prettify())

    # Career

    myuls = soup.find_all("ul", {"class": "experience__list"}, limit=2)

    text_single_job = myuls[0].find_all("li", {"class": "profile-section-card experience-item"})  # li  for list item
    text_group_job = myuls[0].find_all("li", {"class": "experience-group experience-item"})  # li  for list item

    # Education

    myuls = soup.find_all("ul", {"class": "education__list"}, limit=2)

    text_single_study = myuls[0].find_all("li",
                                          {"class": "profile-section-card education__list-item"})  # li  for list item
    # text_group = myuls[0].find_all("li", {"class": "experience-group experience-item"})  # li  for list item

    # Name & co

    identity_raw = soup.find_all("div", {"class": "top-card-layout__entity-info"})
    len(identity_raw)

    print(len(text_single))
    print(len(text_group))
    for li in text:  # list item
        print(li.find_next("h3").text)
        print(li.find_next("h4").text)
        print(li.find_next("time").text)  # find newt gives the first one from where the object is pointing
        print(li.find_next("time").find_next("time").text)

    len(text[0].find_all("time"))
    text[0].find_all("time")
    text[0].find_all({"experience-group experience-item"})
    text[0].find_all("class")
    len(myuls[0].find_all("li", {"class": "experience-group experience-item"}))

    len(myuls[0].find_all("li")[
            myuls[0].find_all("li") == myuls[0].find_all("li", {"class": "experience-group experience-item"})])

    text.single[0].find_next("h3").text

    str.strip(text.single[0].find_next("h3").text)
    str.strip(text.single[0].find_next("h4").text)

    try:
        assert (text.single[0].get("data-section") in ('pastPositionsDetails', 'currentPositionsDetails'))

        if (text.single[0].get("data-section") == 'pastPositionsDetails'):
            text.single[0].find_next("time").text
            text.single[0].find_next("time").find_next("time").text
        elif (text.single[0].get("data-section") == 'currentPositionsDetails'):
            text.single[0].find_next("time").text

    except AssertionError:
        print("'data-section' not 'pastPositionsDetails' or 'currentPositionsDetails' -> Not possible")

    for i in text[3].find_all("time"):
        print(i.find_next("time").text)

    text.single[0].find_all("li", {"data-section": "pastPositionsDetails"})
    text.single[0].find_next("li")
    text.single[0].get("data-section")
