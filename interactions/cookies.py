from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "key", "value": "value"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Get cookie details with named cookie 'foo'
print(driver.get_cookie("foo"))

# Get all available cookies
print(driver.get_cookies())

# Delete a cookie with name 'test1'
driver.delete_cookie("test1")

#  Deletes all cookies
driver.delete_all_cookies()
  
  