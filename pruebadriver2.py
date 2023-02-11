#!/usr/bin/env python
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.binary_location = "/snap/bin/chromium"
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--verbose')
chrome_options.add_argument('--remote-debugging-port=9222')

service = Service(executable_path="/home/bitsamericas/external/selenium/driver/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://duckduckgo.com/")
title = driver.title
assert "DuckDuckGo" in title

driver.implicitly_wait(10)


search_box = driver.find_element(by=By.NAME, value="q")
search_button = driver.find_element(by=By.ID, value="search_button_homepage")

search_box.send_keys("Selenium")
search_button.click()

search_box = driver.find_element(by=By.NAME, value="q")
value = search_box.get_attribute("value")
assert value == "Selenium"

driver.quit()
print("Hello World")

