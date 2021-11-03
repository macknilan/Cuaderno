"""
Day 16 - Scrape & Automate behind Password Protected Apps with Selenium & Python
🔗 https://youtu.be/3DCtaJvf6VA 
🔗 https://github.com/codingforentrepreneurs/30-Days-of-Python/blob/master/tutorial-reference/Day%2016/insta.py
"""

# import getpass
# the_password = getpass.getpass("Type the password: ")
# print(f"the_password -> {the_password}")
import os
import time
from selenium import webdriver
from conf import INSTA_USERNAME, INSTA_PASSWORD

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Chrome(
    f"{BASE_DIR}/chromedriver_selenium_linux64/chromedriver")
url = "https://www.instagram.com/"
driver.get(url)

time.sleep(2)
usr_name = driver.find_element_by_name("username")
usr_name.send_keys(INSTA_USERNAME)
usr_pwd = driver.find_element_by_name("password")
usr_pwd.send_keys(INSTA_PASSWORD)

time.sleep(2)
submit_btn = driver.find_element_by_css_selector("button[type='submit']")
submit_btn.click()


def click_to_follow(driver):
    # https://www.w3schools.com/xml/xpath_syntax.asp
    # Chrome extension SelectorsHub
    # Chrome extension ChroPath
    # my_follow_btn_xpath = "//a[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    # my_follow_btn_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    follow_btn_elments = driver.find_elements_by_xpath(my_follow_btn_xpath)
    for btn in follow_btn_elments:
        time.sleep(2)  # self-throttle
        try:
            btn.click()
        except:
            pass


time.sleep(2)
url_to_folow = "https://www.instagram.com/ted/"
driver.get(url_to_folow)
click_to_follow(driver)
