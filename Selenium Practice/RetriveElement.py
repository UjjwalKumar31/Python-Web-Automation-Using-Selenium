from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')

# Find an element by ID (use the new method)
element_id = driver.find_element(By.ID, 'js-link-box-en')
print(f'{element_id = }')

# # Find an element by name
# element_name = driver.find_element(By.NAME, 'q')
# print(f'{element_name = }')

# Correct the XPath to properly select the first h2 element under the mainContent
heading_xpath = driver.find_element(By.XPATH, "//*[@id='js-link-box-en']/strong")
print(f'{heading_xpath = }')

# Find an element by class name
element_classname = driver.find_element(By.CLASS_NAME, 'link-box')
print(f'{element_classname = }')

# Close the driver
driver.close()

#######################################################################################################

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://selenium.dev')

# Find an element by ID (use the new method)
element_id = driver.find_element(By.ID, 'td-block-0')
print(f'{element_id = }')

# # Find an element by name
# element_name = driver.find_element(By.NAME, 'submit')
# print(f'{element_name = }')

# Correct the XPath to properly select the first h2 element under the mainContent
heading_xpath = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div/div/h1")
print(f'{heading_xpath = }')

# Find an element by class name
element_classname = driver.find_element(By.CLASS_NAME, 'fw-bold')
print(f'{element_classname = }')

driver.close()

#######################################################################################################

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://www.python.org/')

# Find an element by ID (use the new method)
element_id = driver.find_element(By.ID, 'submit')
print(f'{element_id = }')

# # Find an element by name
element_name = driver.find_element(By.NAME, 'submit')
print(f'{element_name = }')

# Correct the XPath to properly select the first h2 element under the mainContent
heading_xpath = driver.find_element(By.XPATH, "//*[@id='touchnav-wrapper']/header/div/h1/a/img")
print(f'{heading_xpath = }')

# Find an element by class name
element_classname = driver.find_element(By.CLASS_NAME, 'search-button')
print(f'{element_classname = }')

driver.close()
