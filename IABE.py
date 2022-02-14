from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

prefix_member = 'https://iabe.be/about-iabe/members/public-member-list'
prefix_qualified_member = 'https://iabe.be/about-iabe/iabe-qualified-members'

links_member = [prefix_member]
links_qualified_member = [prefix_qualified_member]

for i in range(8):
    new_link = str(prefix_qualified_member) + str('?pager=') + str(i+2)
    links_qualified_member.append(new_link)

for i in range(22):
    new_link = str(prefix_member) + str('?pager=') + str(i+2)
    links_member.append(new_link)

# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get(links_member[0])

soup = BeautifulSoup(driver.page_source, 'html.parser')

mydivs = soup.find_all("div", {"class": "publicRelationList__relation"})
mydivs[0].find_next("h3").text.replace(",","")

list_member = []
from selenium.webdriver.support.ui import WebDriverWait
for i in range(len(links_member)):
    driver.get(links_member[i])
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    mydivs = soup.find_all("div", {"class": "publicRelationList__relation"})

    for i in range(len(mydivs)):
        list_member.append(mydivs[i].find_next("h3").text.replace(",", " "))

print('Finished')

list_qualified_member = []
from selenium.webdriver.support.ui import WebDriverWait
for i in range(len(links_qualified_member)):
    driver.get(links_qualified_member[i])
    # time.sleep(3)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "variantDefault"))
    )
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    mydivs = soup.find_all("div", {"class": "publicRelationList__relation"})

    for i in range(len(mydivs)):
        list_qualified_member.append(mydivs[i].find_next("h3").text.replace(",", " "))

print('Finished')

