#!/usr/bin/env python
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def get_driver():
    chrome_options = Options()
    chrome_options.binary_location = "/snap/bin/chromium"
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--verbose')
    chrome_options.add_argument('--remote-debugging-port=9222')

    service = Service(executable_path="/home/bitsamericas/external/selenium/driver/chromedriver_linux64/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


