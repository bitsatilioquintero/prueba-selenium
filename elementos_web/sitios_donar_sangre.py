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
url = "http://www.saludcapital.gov.co/DDS/Paginas/Donde-puedo-donar-sangre.aspx" 
driver.get(url)

title = driver.title
assert "Sangre" in title

home = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.ID, "aspnetForm"))
home.find_element(By.LINK_TEXT, "aquí").click()

years = driver.find_elements(By.XPATH, "//table[@id='ctl07_GVPUNTOSMOVILES']/tbody/tr/td[1]")
months = driver.find_elements(By.XPATH, "//table[@id='ctl07_GVPUNTOSMOVILES']/tbody/tr/td[2]")
days = driver.find_elements(By.XPATH, "//table[@id='ctl07_GVPUNTOSMOVILES']/tbody/tr/td[3]")
address = driver.find_elements(By.XPATH, "//table[@id='ctl07_GVPUNTOSMOVILES']/tbody/tr/td[4]")
max_rows = len(address)
date = get_date()

print("== SITIOS DONDE DONAR ==")
for j in range(max_rows):
    if (years[j].text == date["year"] and months[j].text == str(date["month"]) and days[j].text == str(date["day"])):
        print(address[j].text)

driver.close()
driver.quit()
print("Rock the baby")
