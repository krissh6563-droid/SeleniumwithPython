from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Navigate to
driver.get("https://selenium.dev")

# back
driver.back()

# forward
driver.forward()

# refresh
driver.refresh()