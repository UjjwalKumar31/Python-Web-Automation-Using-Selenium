from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://wiki.python.org/moin/FrontPage')

search_box = driver.find_element(By.ID, 'searchinput')
search_box.clear()                  #Clear pre-existing inputs
search_box.send_keys("Beginner")       #To send the input at search
search_box.send_keys(Keys.RETURN)   #To hit ENTER to get response
sleep(5)

from selenium.webdriver.support.ui import Select

select = Select(driver.find_element(By.XPATH, "//*[@id='sidebar']/div[3]/ul/li[5]/form/div/select"))    # XPATH --> '//*/form/div/select'
select.select_by_visible_text("Raw Text")
sleep(15)

driver.close()