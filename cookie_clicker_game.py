from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys

import time


options = Options()
options.add_experimental_option("detach", True)
driver = selenium.webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
buyable_items_prices = driver.find_elements(By.CSS_SELECTOR, "div b")
for item in buyable_items_prices:
    print(item.text)

# while True:
#
#     cookie.click()
#     money = driver.find_element(By.CSS_SELECTOR, "#money").text
