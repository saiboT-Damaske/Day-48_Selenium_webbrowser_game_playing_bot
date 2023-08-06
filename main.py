from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

service = Service("C:\Development\chromedriver.exe")

# these options keep the window from closing automatically
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)

# ------------------- find element by class name -------------------- #

# driver.get("https://www.amazon.de/dp/B07M5HX7VS/ref=twister_B0B7JLYPVY?_encoding=UTF8&th=1&psc=1")
# # price = driver.find_element(By.CLASS_NAME, "a-price-whole")     # also works but only whole number
# price = driver.find_element(By.CLASS_NAME, "a-price")
# print(price.text.replace("\n", "."))
# price_float = float(price.text.replace("\n", ".").replace("€", ""))


# --------------- find element by name --------------------------- #
# driver.get("https://python.org")
#
# by_name = driver.find_element(By.NAME, "q")
# print(by_name.get_attribute("placeholder"))     # or name or text.

# ---------------- find element by css -------------------------- #
# driver.get("https://python.org")
#
# doc_link = driver.find_element(By.CSS_SELECTOR, ".small-widget.documentation-widget a")
# print(doc_link.get_attribute("href"))
#
# x_patch = driver.find_element(By.XPATH, "/html/body/div/footer/div[2]/div/ul/li[2]/a")
# print(x_patch.get_attribute("href"))

# ---------------- find elements ---------------------------- #
driver.get("https://python.org")
# python_events = {
#     "date": {},
#     "name": {},
#     "link": {},
# }
#
# dates = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/time")
# for event in dates:
#     date = event.get_attribute("datetime").split("T")[0]
#     python_events["date"].append(date)
#
#
#
#
# names = driver.find_elements(By.CSS_SELECTOR, ".event-widget > div:nth-child(1) > ul:nth-child(3) > li > a:nth-child(2)")
# for event in names:
#     link = event.get_attribute("href")
#     name = event.get_attribute("text")
#     python_events["name"].append(name)
#     python_events["link"].append(link)
#
# print(python_events)

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for date in dates:
    print(date.get_attribute("datetime").split("T")[0])

names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for name in names:
    print(name.text)

events = {}
for n in range(len(names)):
    events[n] = {
        "time": dates[n].get_attribute("datetime").split("T")[0],
        "name": names[n].text,
    }

print(events)

# these options ensure the window closes at the end of the session
# driver.close()  # close tab
driver.quit()   # quit entire program
