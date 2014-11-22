from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_condition
from selenium.webdriver.common.by import By
import unittest

class WaitForElements(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome
        driver.get("http://www.travelingtony.weebly.com")

    def test_WaitForCheckoutPhhotoButton(self):
        locator = "//span[.='Check out my coolest photos']"
        seebutton = WebDriverWait(driver, 10).until(expected_condition.presence_of_element_located(By.XPATH, locator))

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()