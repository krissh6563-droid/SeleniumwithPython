# Given one website URL and asked to capture text of element and print the same 
# for 10 times and print average time to load website for 10 times

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def capture_text(url):
    start_time = time.time()
    driver = webdriver.Chrome()
    driver.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    
    try:
        element = driver.find_element(By.ID, '')
        if element:
            text = element.text.strip()
            print(text)
        else:
            print("Element not found")

    except Exception as e:
        print(f"Error {e}")

    driver.quit()
    return load_time


def main():
    url = "https://www.w3schools.com/"
    total_load_time = 0
    for i in range(10):
        load_time = capture_text(url)
        total_load_time = total_load_time + load_time
    
    avg_load_time = total_load_time/10
    print(f"\nAverage time to load website for 10 times: {avg_load_time} seconds")



if __name__ == "__main__":
    main()

