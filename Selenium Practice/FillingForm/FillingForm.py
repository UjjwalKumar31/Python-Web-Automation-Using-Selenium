from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:3000/Selenium Practice/FillingForm/form.html')

select = Select(driver.find_element(By.NAME, 'numReturnSelect'))
select.select_by_index(4)
time.sleep(5)

select.select_by_visible_text("200")
time.sleep(5)

select.select_by_value("15000")
time.sleep(5)

options = select.options
print(options)

submit_button = driver.find_element(By.NAME, 'continue')
submit_button.submit()
time.sleep(5)

driver.close()
