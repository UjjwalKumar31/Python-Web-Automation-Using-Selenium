from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://python.org')

search = driver.find_element(By.NAME, 'q')
search.clear()                  #Clear pre-existing inputs
search.send_keys("pycon")       #To send the input at search
search.send_keys(Keys.RETURN)   #To hit enter to get response

time.sleep(5)

driver.close()