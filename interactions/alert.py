from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert

import time

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/documentation/webdriver/interactions/alerts/")


################## ALERT ##########################
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

# Wait for the alert to be displayed and store it in a variable
wait = WebDriverWait(driver, 10)
alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()


####################### Confirm ######################

# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample confirm").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = driver.switch_to.alert

# Store the alert text in a variable
text = alert.text

# Press the Cancel button
alert.dismiss()
  
####################### Promt ##############################

# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = Alert(driver)

# Type your message
alert.send_keys("Selenium")

# Press the OK button
alert.accept()
  
  