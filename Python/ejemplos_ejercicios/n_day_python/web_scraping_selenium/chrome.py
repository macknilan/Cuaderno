# https://sites.google.com/chromium.org/driver/home
# https://selenium-python.readthedocs.io/

import os
import time
from selenium import webdriver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"BASE_DIR -> {BASE_DIR}")


driver = webdriver.Chrome(
    f"{BASE_DIR}/chromedriver_selenium_linux64/chromedriver")
url = "https://www.google.com/"
driver.get(url)
# SUSPENDS (DELAYS) EXECUTION OF THE CURRENT THREAD FOR THE GIVEN NUMBER OF SECONDS.
time.sleep(2)
search_box = driver.find_element_by_name("q")
search_box.send_keys("python selenium")

submit_btn_el = driver.find_element_by_css_selector("input[type='submit']")
print(f"Name of the button -> {submit_btn_el.get_attribute('name')}")

time.sleep(2)
submit_btn_el.click()

time.sleep(5)
driver.quit()
