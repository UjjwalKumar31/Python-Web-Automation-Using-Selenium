from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver2 = webdriver.Firefox()
driver3 = webdriver.Edge()

driver.get("http://seleniumhq.org")
driver2.get("http://seleniumhq.org")
driver3.get("http://seleniumhq.org")

sleep(30)

driver.close()