
# from selenium import webdriver

# PATH = "/usr/local/bin/chromedriver.exe"


# driver = webdriver.Chrome(PATH)

# driver.get("https://google.com")

	# !/usr/bin/python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests 
from bs4 import BeautifulSoup
import io
import time





Path = "/usr/local/bin/chromedriver.exe"#chromedriver path

driver = webdriver.Chrome()#open browser

driver.get("https://www.dcard.tw/f")

print(driver.title)

search = driver.find_element(By.NAME, "query" )
search.clear()
search.send_keys("比特幣")
# time.sleep(3)
search.send_keys(Keys.RETURN)
# time.sleep(3)
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "atm_26_loj7t9"))
    )



titles = driver.find_elements(By.CLASS_NAME, "atm_cs_1urozh")
for title in titles :
    print(title.text)

# link = driver.find_element(By.LINK_TEXT, "手頭突然拿到六千元 怎麼規劃")
# link.click()#點擊連結
# driver.back()#回上一頁
# driver.forward()#回下一頁

time.sleep(10)

driver.quit()


