from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.example.com")

ele = driver.find_element(By.CSS_SELECTOR, 'h1')

    # Returns and base64 encoded string into image
ele.screenshot('./image.png')

driver.quit()
  