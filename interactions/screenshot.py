from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')

driver.quit()