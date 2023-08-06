from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys

options = Options()
options.add_experimental_option("detach", True)
driver = selenium.webdriver.Chrome(options=options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Hans")
first_name = driver.find_element(By.NAME, "lName")
first_name.send_keys("Peter")
first_name = driver.find_element(By.NAME, "email")
first_name.send_keys("yoyo@gmail.com", selenium.webdriver.common.keys.Keys.ENTER)

# # or this in the end
# button = driver.find_element(By.CSS_SELECTOR, "form button")
# button.click()

