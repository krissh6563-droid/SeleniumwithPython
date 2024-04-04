from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
url = "https://orange-corabelle-71.tiiny.site/"


driver.find_element(By.CLASS_NAME, 'information')
driver.find_element(By.CSS_SELECTOR, "#fname")
driver.find_element(By.ID, "lname")
driver.find_element(By.NAME, "newsletter")
driver.find_element(By.LINK_TEXT, "Selenium Official Page")
driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
driver.find_element(By.TAG_NAME, "a")
driver.find_element(By.XPATH, "//input[@value='f']")
