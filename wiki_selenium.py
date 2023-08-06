from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_amount = driver.find_element(By.XPATH,
# "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")
# print(article_amount.text)

article_amount_2 = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_amount_2.click()

all_portals = driver.find_element(By.LINK_TEXT, "View source")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)
