# https://sites.google.com/chromium.org/driver/home
# https://selenium-python.readthedocs.io/

import os
import time

from selenium import webdriver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(f"BASE_DIR -> {BASE_DIR}")


driver = webdriver.Chrome(f"{BASE_DIR}/chromedriver_selenium_linux64/chromedriver")
driver.get("http://www.google.com/")
# SUSPENDS (DELAYS) EXECUTION OF THE CURRENT THREAD FOR THE GIVEN NUMBER OF SECONDS.
time.sleep(5)
driver.quit()
