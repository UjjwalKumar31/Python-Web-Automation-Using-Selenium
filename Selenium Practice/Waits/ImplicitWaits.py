from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)      #Waits for site to load for 10 sec and then for each element 10 secs

driver.get('http://www.python.org')

myDynamicElement = driver.find_element(By.ID, 'start-shell')

driver.close()

'''Note: Implicit waits are used to wait until a certain time period before every action in the script is performed.'''