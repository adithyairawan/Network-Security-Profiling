import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome('/home/adit/Downloads/chromedriver', chrome_options=options)

# Test name: test1
driver.get("http://modem.wifi/")
driver.set_window_size(1366, 741)
driver.find_element(By.CSS_SELECTOR, ".btn-tologin").click()
# Step # | name | target | value
# 3 | type | id=user | admin
driver.find_element(By.ID, "user").send_keys("admin")
# 4 | click | id=pwd | 
driver.find_element(By.ID, "pwd").click()
# 5 | type | id=pwd | admin
driver.find_element(By.ID, "pwd").send_keys("admin")
# 6 | click | id=login | 
driver.find_element(By.ID, "login").click()
driver.find_element(By.CSS_SELECTOR, ".home-traffic > .home-icon-text-div").click()
# 9 | click | linkText=MAC Filter | 
driver.find_element(By.LINK_TEXT, "MAC Filter").click()
# 10 | mouseOver | linkText=MAC Filter | 
element = self.driver.find_element(By.LINK_TEXT, "MAC Filter")
actions = ActionChains(self.driver)
actions.move_to_element(element).perform()
# 11 | mouseOut | linkText=MAC Filter | 
element = self.driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(self.driver)
actions.move_to_element(element, 0, 0).perform()
# 12 | click | id=to_login | 
driver.find_element(By.ID, "to_login").click()
