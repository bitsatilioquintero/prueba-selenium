#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pprint import pprint

chrome_options = Options()
chrome_options.binary_location = "/snap/bin/chromium"
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--verbose')
chrome_options.add_argument('--remote-debugging-port=9222')

keyword = input("Enter a keyword to search:\n")

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)
driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

search_box = driver.find_element(By.NAME, 'search')
search_box.send_keys(keyword)
search_box.send_keys(Keys.ENTER)

time.sleep(3)

# take a screenshot
driver.save_screenshot("image.png")
main_data = driver.find_element(By.ID, 'content')
print(main_data.text)

driver.quit()
print('OK');
