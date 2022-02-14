# https://www.geeksforgeeks.org/performing-google-search-using-python-code/

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "site:linkedin.com " + "Gaetan Gellens"

for j in search(query, tld="co.in", num=10, stop=1, pause=2, country="Belgium"):
    print(j)
    a = j

# import web driver


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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

# soup.find_all("a")
# mydivs = soup.find_all("div", {"class": "core-section-container__content"}, limit=1)
# ul = mydivs[0].find_next("ul") # unordinated
# text = ul.find_all("li") # li  for list item
# print(len(text))
# for li in text: # list item
#     print(li.find_next("h3").text)
#     print(li.find_next("h4").text)
#     print(li.find_next("time").text) # find newt gives the first one from where the object is pointing
#     print(li.find_next("time").find_next("time").text)

# This is for the second part
# mydivs = soup.find_all("div", {"class": "core-section-container__content"}, limit=2)
# ul = mydivs[1].find_next("ul") # unordinated
# text = ul.find_all("li") # li  for list item
# print(len(text))
# for li in text: # list item
#     print(li.find_next("h3").text)
#     print(li.find_next("h4").text)
#     print(li.find_next("time").text) # find newt gives the first one from where the object is pointing
#     print(li.find_next("time").find_next("time").text)
# # mydivs[0].find_next("h3").find_next("h3")

# Career

myuls = soup.find_all("ul", {"class": "experience__list"}, limit=2)

text_single = myuls[0].find_all("li", {"class": "profile-section-card experience-item"})  # li  for list item
text_group = myuls[0].find_all("li", {"class": "experience-group experience-item"})  # li  for list item

# Education

myuls = soup.find_all("ul", {"class": "education__list"}, limit=2)

text_single = myuls[0].find_all("li", {"class": "profile-section-card education__list-item"})  # li  for list item
# text_group = myuls[0].find_all("li", {"class": "experience-group experience-item"})  # li  for list item

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
