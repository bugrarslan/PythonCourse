from selenium import webdriver
import time

driver = webdriver.Edge()

url = "https://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "https://github.com/bugrarslan"
driver.get(url)

print(driver.title)

if "bugrarslan" in driver.title:
    driver.save_screenshot("github-bugrarslan.png")

time.sleep(2)

driver.back()
time.sleep(2)

driver.close()
