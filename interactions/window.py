from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "new window").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))


# Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
driver.switch_to.new_window('window')

#Close the tab or window
driver.close()

#Switch back to the old tab or window
driver.switch_to.window(original_window)


  
  
  