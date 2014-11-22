from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_condition
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
locator = driver.find_element_by_css_selector("#gbqfq")

try:
    search = WebDriverWait(driver, 10).until(expected_condition.presence_of_element_located(By.CSS_SELECTOR, locator))
finally:
    driver.quit()
