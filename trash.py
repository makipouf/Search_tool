from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/username/bin/chromedriver')
driver = webdriver.Chrome('/application/Chromedriver/chromedriver')
driver = webdriver.Chrome('/application/Chromedriver')
driver = webdriver.Chrome("/Program Files/mingw-w64/x86_64-8.1.0-win32-seh-rt_v6-rev0/mingw64/bin")
driver = webdriver.Chrome(executable_path=r"C:/Users/gaeta/PycharmProjects/Search_tool/chromedriver.exe")
driver = webdriver.Chrome(executable_path=r"C:\Users\gaeta\PycharmProjects\Search_tool\chromedriver.exe")
driver = webdriver.Chrome(executable_path= "C:\\Windows\\chromedriver.exe")

search_query = driver.find_element_by_name('btnK')
search_query.submit

first_request = driver.find_elements_by_xpath('//*[@class="yuRUbf"]/a[@href]')
first_request = driver.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div')
yuRUbf

driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

driver.quit()

driver = webdriver.Chrome()


driver.get("http://www.google.com")
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "q")))
element.send_keys("selenium")
element.send_keys(Keys.ENTER)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='search']//div[@class='g']/div[@class='rc']/div[@class='r']/a"))).click()

h3headers
soup.title
soup.title.name

soup.title.parent.name

soup.p
soup.p['cta-modal__header']
soup.find_all('a')



# .send_keys() to simulate the return key
search_query.send_keys(Keys.RETURN)

driver.get('https://hoopshype.com/salaries/players/')
driver.get('https://be.linkedin.com/in/ga%C3%A9tan-gellens-705243180')

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
datetime_beginning = datetime.strptime('Jun 2005', '%b %Y')
length = datetime.strptime('Jun 2005', '%b %Y')-datetime.strptime('Jun 2004', '%b %Y')
length1 = datetime.strptime('Jun 2004', '%b %Y')-datetime.strptime('Jun 2005', '%b %Y')
length1.days

# print(self.name)
# print(self.company)
# print(str(self.beginning()))
# print(str(self.ending()))

from webdriver_manager.firefox import GeckoDriverManager

len(text_group[0].find_all("li"))
list_job = list()
list_li = text_group[0].find_all("li")
new_job = Job()
new_job.change_company_name(str.strip(text_group[0].find_next("h4").text))
new_job.change_job_name(str.strip(list_li[0].find_next("h3").text))
new_job.change_job_name(str.strip(list_li[1].find_next("h3").text))


len(text_single[0].find_next("h4").contents)
re.search(">(.*?)<", str(text_single[0].find_next("h4").contents[2])).group(1)
re.search("<time>(.*?)</time>", str(text_single[0].find_all("p", {"class": "education__item education__item--duration"}, limit=2)[0])).group(1)
re.findall("<time>(.*?)</time>", str(text_single[0].find_all("p", {"class": "education__item education__item--duration"}, limit=2)[0]))

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

This is for the second part
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

    def beginning(self):

        time_beginning_ini = self.time_beginning
        return time_beginning_ini.strftime("%B %Y")

    def ending(self):

        time_ending_ini = self.time_ending
        return time_ending_ini.strftime("%B %Y")

    def length(self):

        try:
            assert ((self.time_ending - self.time_beginning).days >= 0)
            length = self.time_ending - self.time_beginning
            # return divmod(length.total_seconds(), 31536000)[0]
            return round(length.total_seconds() / 31536000, 1)

        except AssertionError:
            print("The length is negative -> Not possible")

    def __repr__(self):

        # return {'Job name':self.name, 'Company':self.company}
        return ''

        # send_keys() to simulate the search text key strokes
        # search_query.send_keys('site:linkedin.com "Gaétan Gellens"')
        # search_query.send_keys('site:linkedin.com "Rubin Daija"')
        # search_query.send_keys('site:linkedin.com "Meghna Lakshminarayanan"')



