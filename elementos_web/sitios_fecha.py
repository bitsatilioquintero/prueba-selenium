#!/usr/bin/env python
from ini_selenium import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import datetime

def get_date():
    today = datetime.datetime.now()
    day = int(today.strftime("%d"))
    month = int(today.strftime("%m"))
    year = today.strftime("%Y")
    mydict = {
        "day": day,
        "month": month,
        "year": year
    }
    return mydict

driver = get_driver();
url = "file:///home/bitsamericas/external/selenium/elementos_web/Red_Sangre.html" 
driver.get(url)
table = driver.find_element(By.ID, "ctl07_GVPUNTOSMOVILES")
years = table.find_elements(By.XPATH, "//table[@id='ctl07_GVPUNTOSMOVILES']/tbody/tr/td[1]")
months = table.find_elements(By.XPATH, "//table[@id='ctl07_GVPUNTOSMOVILES']/tbody/tr/td[2]")
days = table.find_elements(By.XPATH, "//table[@id='ctl07_GVPUNTOSMOVILES']/tbody/tr/td[3]")
address = table.find_elements(By.XPATH, "//table[@id='ctl07_GVPUNTOSMOVILES']/tbody/tr/td[4]")
max_rows = len(address)
date = get_date()
print("== SITIOS DONDE DONAR ==")
for j in range(max_rows):
    if (years[j].text == date["year"] and months[j].text == str(date["month"]) and days[j].text == str(date["day"])):
        print(address[j].text)
driver.quit()
print("\nRock the baby")
