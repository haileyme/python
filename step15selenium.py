# Auto-search at Youtube using Selenium

# pip install selenium==3.0
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\driver\chromedriver.exe')
driver.get('http://www.youtube.com')
tag = driver.find_element_by_name('search_query')
tag.clear()
tag.send_keys('Christmas')
tag.submit()

driver.get('http://www.naver.com')
tag = driver.find_element_by_name('query')
tag.clear()
tag.send_keys('Christmas')
tag.submit()

time.sleep(30)
driver.close()
