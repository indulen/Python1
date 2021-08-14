from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('https://www.google.com/')
driver.set_page_load_timeout(10)
searchbox = driver.find_element_by_name('q').send_keys('Selenium',Keys.ENTER)
print(driver.title)
print(driver.current_url)
driver.close()

driver = webdriver.Firefox()
driver.get('https://www.google.com/')
driver.set_page_load_timeout(20)
searchbox = driver.find_element_by_name('q').send_keys('Python',Keys.ENTER)


