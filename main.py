from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")


items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

five_second = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > five_second:

        prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []
        for price in prices:
            try:
                # item = price.text.split("-")[0]
                item_price = int(price.text.split("-")[1].replace(",", "").strip())
                # print(item)
                item_prices.append(item_price)
            except IndexError:
                pass

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        try:
            money = int("".join(driver.find_element_by_id("money").text.replace(",", " ").strip()))
        except ValueError:
            pass

        available_upgrades = {}
        for price, id in cookie_upgrades.items():
            if money > price:
                available_upgrades[price] = id

        highest_upgrade = max(available_upgrades)
        # print(highest_upgrade)
        highest_id = available_upgrades[highest_upgrade]

        driver.find_element_by_id(highest_id).click()

        five_second = time.time() + 5

    if time.time() > five_min:
        cookie_per_second = driver.find_element_by_id("cps").text
        print(cookie_per_second)
        break


