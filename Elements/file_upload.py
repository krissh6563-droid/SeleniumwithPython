from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


def test_uploads(driver, upload_file):
    driver.get("https://the-internet.herokuapp.com/upload")
    #upload_file = os.path.abspath(
    #    os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png"))
    time.sleep(5)

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(upload_file)
    driver.find_element(By.ID, "file-submit").click()
    time.sleep(5)

    file_name_element = driver.find_element(By.ID, "uploaded-files")
    file_name = file_name_element.text

    assert file_name == "Screenshot.png"


def main():
    driver = webdriver.Chrome()
    upload_file = "C:/Users/krish/Desktop/Screenshot.png"
    test_uploads(driver, upload_file)


if __name__ == "__main__":
    main()
