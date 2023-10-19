from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests 
from bs4 import BeautifulSoup
import io
import time

ath = "/usr/local/bin/chromedriver.exe"#chromedriver path

driver = webdriver.Chrome()#open browser

driver.get("https://webapp.yuntech.edu.tw/YunTechSSO/Account/Login")

print(driver.title)

search1 = driver.find_element(By.NAME, "pLoginName" )
search1.send_keys("B11036014")
search2 = driver.find_element(By.NAME, "pLoginPassword" )
search2.send_keys("maxlin920410")
search2.send_keys(Keys.RETURN)

time.sleep(3)
link = driver.find_element(By.LINK_TEXT, "學期選課資料")
link.click()
link2 = driver.find_element(By.NAME, "ctl00$MainContent$PrintButton")
link2.click()




time.sleep(10)

driver.quit()