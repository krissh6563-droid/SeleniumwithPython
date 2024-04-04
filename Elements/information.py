from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

#is displayed
    # Get boolean value for is element display
is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()

# is enabled
    # Returns true if element is enabled else returns false
value = driver.find_element(By.NAME, 'button_input').is_enabled()

# is selected 
    # Returns true if element is checked else returns false
value = driver.find_element(By.NAME, "checkbox_input").is_selected()

# tag name
    # Returns TagName of the element
attr = driver.find_element(By.NAME, "email_input").tag_name

# size and position
    # Returns height, width, x and y coordinates referenced element
res = driver.find_element(By.NAME, "range_input").rect

# get css value
    # Navigate to Url
driver.get('https://www.selenium.dev/selenium/web/colorPage.html')
    # Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element(By.ID, "namedColor").value_of_css_property('background-color')

#text content
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/linked_image.html")

    # Retrieves the text of the element
text = driver.find_element(By.ID, "justanotherlink").text

# Fetching Attributes or Properties

    # Identify the email text box
email_txt = driver.find_element(By.NAME, "email_input")

    # Fetch the value property associated with the textbox
value_info = email_txt.get_attribute("value")
  
  


