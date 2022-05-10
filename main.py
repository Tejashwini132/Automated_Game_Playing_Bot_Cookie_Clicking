from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("start-maximized")
chrome_drive_path = "C:\Development\chromedriver.exe"
ser = Service(chrome_drive_path)
driver = webdriver.Chrome(service=ser, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
clicking_cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
clicking_cookie.click()
item_ids = [item.get_attribute("id") for item in items]
timeout = time.time() + 5
one_min = time.time() + 60 * 5

while True:
    clicking_cookie.click()
    if time.time() > timeout:
        all_price = (driver.find_elements(By.CSS_SELECTOR, "#store b"))
        item_price = []

        for price in all_price:
            element_text = price.text
            if element_text != "":
                cost = element_text.split("-")[1].strip().replace(",", "")
                item_price.append(int(cost))

        cookie_upgrade = {}
        for n in range(len(item_price)):
            cookie_upgrade[item_price[n]] = item_ids[n]

        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        affordable_upgrade = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrade[cost] = id

        highiest_price_affordable_upgrade = max(affordable_upgrade)
        print(highiest_price_affordable_upgrade)
        to_purchase = affordable_upgrade[highiest_price_affordable_upgrade]

        timeout = time.time() + 5

        if time.time() > one_min:
            cookie_per = driver.find_element(By.ID, "cps").text
            print(cookie_per)
            break