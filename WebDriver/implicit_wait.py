from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.implicitly_wait(15)

driver.get("http://www.google.com")

locator = driver.find_element_by_css_selector("#gbqfq")
locator.send_keys("selenium")
sleep(5)
driver.quit()