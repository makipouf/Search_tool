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





