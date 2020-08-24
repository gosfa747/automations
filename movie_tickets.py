import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10) # seconds
driver.get('https://www.eventcinemas.com.au/');


# select city
button = driver.find_element_by_xpath('/html/body/header/div[3]/div[2]')
button.click()

button = driver.find_element_by_xpath('/html/body/header/div[3]/div[3]/div/div[1]/div')
button.click()

button = driver.find_element_by_xpath('/html/body/header/div[3]/div[3]/div/div[2]/div[2]/div/div/span[1]')
button.click()

button = driver.find_element_by_xpath('/html/body/header/div[3]/div[3]/div/div[2]/div[3]/div[1]/a[14]/div')
button.click()


#select movie
button = driver.find_element_by_xpath('/html/body/header/div[1]/div')
button.click()

button = driver.find_element_by_xpath('/html/body/nav/div[2]/a')
button.click()

button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/a/div[2]')
button.click()


#add cinema
button = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[3]/span')
button.click()

button = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[3]/div/div[2]/div/div[1]/div[14]/a/div')
button.click()

button = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[3]/div/div[3]/a')
button.click()

#find session time
button = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[2]/div/div[2]/div[1]/div/ul/li[1]/div[2]/div[2]/div[1]/div/a[4]/span[2]/span[2]')
button.click()


#choose your seats
button = driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[1]/div[2]/div[3]/div/div[4]/div/div/ul[7]/li[13]')
button.click()

button = driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[1]/div[2]/div[3]/div/div[4]/div/div/ul[7]/li[14]')
button.click()

button = driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[1]/div[2]/div[4]/div[2]/a')
button.click()

#choose number of tickets and type
button = driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[2]/div[2]/div[2]/div[1]/div[3]/div/table/tbody/tr[6]/td[3]/a[2] ')
button.click()
button.click()

button = driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[2]/div[2]/div[2]/div[5]/a')
button.click()

#Buy frozen coke
button = driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[3]/div[3]/div[2]/div[2]/div[5]/div[2]/div/div/div[1]/a[2]')
button.click()

#proceed to payment
button = driver.find_element_by_xpath("/html/body/div[3]/div/div[4]/div[3]/div[4]/a")
driver.execute_script("arguments[0].click();", button);
