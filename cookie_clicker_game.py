from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys

import time


options = Options()
options.add_experimental_option("detach", True)
driver = selenium.webdriver.Chrome(options=options)
# driver.maximize_window()

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
buyable_items_prices = driver.find_elements(By.CSS_SELECTOR, "div b")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

item_prices = []
prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
for price in prices:
    if price.text != "":
        item_prices.append(int(price.text.strip().split(" - ")[1].replace(",", "")))

# Create dictionary of store items and prices
cookie_upgrades = {}
for n in range(len(item_prices)):
    cookie_upgrades[item_prices[n]] = item_ids[n]

print(cookie_upgrades)


timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:

    cookie.click()
    money = int(driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", ""))



    if time.time() > timeout:
        affordable = {}
        for pr, item_id in cookie_upgrades.items():
            if money >= pr:
                affordable[pr] = item_id

        highest_price_affordable = max(affordable)
        print(highest_price_affordable)

        driver.find_element(By.ID, cookie_upgrades[highest_price_affordable]).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps")
        print(cookie_per_s.text)
        break



