from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# ID = "id"
# NAME = "name"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

url = "https://example.com"
css_selector = ""
driver = webdriver.Chrome()
driver.get(url)
parameter_element = driver.find_element(By.ID, '')
parameter_value = parameter_element.get_attribute("value")
print("value of the parameter", parameter_value)
driver.quit()