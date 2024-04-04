from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Click on the element 
driver.find_element(By.NAME, "color_input").click()

# Clear field to empty it from any previous data
driver.find_element(By.NAME, "email_input").clear()

# Enter Text
driver.find_element(By.NAME, "email_input").send_keys("admin@localhost.dev" )
  
