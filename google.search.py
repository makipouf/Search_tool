import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup



# https://www.geeksforgeeks.org/performing-google-search-using-python-code/

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


from selenium import webdriver
from bs4 import BeautifulSoup
import time

# to search
query = "site:linkedin.com " + "Gaetan Gellens"

for j in search(query, tld="co.in", num=10, stop=1, pause=2, country="Belgium"):
    print(j)
    a = j

# import web driver
from selenium import webdriver



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('http://www.google.be/')

Get_cookies = driver.find_element_by_id('L2AGLb')
Get_cookies.click()
Get_English = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/a[2]')
Get_English.click()



# locate search form by_name
search_query = driver.find_element_by_name('q')
# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com "Gaétan Gellens"')
search_query.send_keys('site:linkedin.com "Rubin Daija"')
search_query.send_keys('site:linkedin.com "ARABI Mouhannad"')
Get_Search = driver.find_element_by_class_name('gNO89b')
Get_Search.submit()

Get_first_request = driver.find_element_by_class_name('yuRUbf')
Get_first_request.click()

driver.back()

Get_first_request = driver.find_element_by_class_name('yuRUbf')
Get_first_request.click()

# Mouhannad Arabi

soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup.prettify())

soup.find_all("a")
mydivs = soup.find_all("div", {"class": "core-section-container__content"}, limit=1)
ul = mydivs[0].find_next("ul") # unordinated
text = ul.find_all("li") # li  for list item
print(len(text))
for li in text: # list item
    print(li.find_next("h3").text)
    print(li.find_next("h4").text)
    print(li.find_next("time").text) # find newt gives the first one from where the object is pointing
    print(li.find_next("time").find_next("time").text)

# This is for the second part
mydivs = soup.find_all("div", {"class": "core-section-container__content"}, limit=2)
ul = mydivs[1].find_next("ul") # unordinated
text = ul.find_all("li") # li  for list item
print(len(text))
for li in text: # list item
    print(li.find_next("h3").text)
    print(li.find_next("h4").text)
    print(li.find_next("time").text) # find newt gives the first one from where the object is pointing
    print(li.find_next("time").find_next("time").text)
# mydivs[0].find_next("h3").find_next("h3")

myuls = soup.find_all("ul", {"class": "experience__list"}, limit=2)
text = myuls[0].find_all("li")
text.single = myuls[0].find_all("li",{"class": "profile-section-card experience-item"}) # li  for list item
text.group = myuls[0].find_all("li",{"class": "experience-group experience-item"}) # li  for list item

print(len(text.single))
print(len(text.group))
for li in text: # list item
    print(li.find_next("h3").text)
    print(li.find_next("h4").text)
    print(li.find_next("time").text) # find newt gives the first one from where the object is pointing
    print(li.find_next("time").find_next("time").text)


len(text[0].find_all("time"))
text[0].find_all("time")
text[0].find_all({"experience-group experience-item"})
text[0].find_all("class")
len(myuls[0].find_all("li", {"class": "experience-group experience-item"}))


len(myuls[0].find_all("li")[myuls[0].find_all("li")==myuls[0].find_all("li",{"class": "experience-group experience-item"})])

text.single[0].find_next("h3").text



str.strip(text.single[0].find_next("h3").text)
str.strip(text.single[0].find_next("h4").text)

try:
    assert (text.single[0].get("data-section") in ('pastPositionsDetails','currentPositionsDetails'))

    if (text.single[0].get("data-section") == 'pastPositionsDetails'):
        text.single[0].find_next("time").text
        text.single[0].find_next("time").find_next("time").text
    elif (text.single[0].get("data-section") == 'currentPositionsDetails'):
        text.single[0].find_next("time").text

except AssertionError:
    print("'data-section' not 'pastPositionsDetails' or 'currentPositionsDetails' -> Not possible")






for i in text[3].find_all("time"):
    print(i.find_next("time").text)

text.single[0].find_all("li",{"data-section": "pastPositionsDetails"})
text.single[0].find_next("li")
text.single[0].get("data-section")


























