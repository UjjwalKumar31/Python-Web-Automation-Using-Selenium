from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.python.org')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'start-shell'))
    )
finally:
    driver.quit()

'''Note : Explicit waits are used to pause the script until a certain condition has been satisfied
    such as the presence of an element, presence of an alert, presence of a frame, etc'''