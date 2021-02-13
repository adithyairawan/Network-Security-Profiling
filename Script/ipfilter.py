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
  
# Test name: test3
# Step # | name | target | value
# 1 | open | / | 
driver.get("http://modem.wifi/")
# 2 | setWindowSize | 683x741 | 
driver.set_window_size(683, 741)
# 3 | click | css=.btn-tologin | 
driver.find_element(By.CSS_SELECTOR, ".btn-tologin").click()
# 4 | type | id=user | admin
driver.find_element(By.ID, "user").send_keys("admin")
# 5 | click | id=pwd | 
driver.find_element(By.ID, "pwd").click()
# 6 | type | id=pwd | admin
driver.find_element(By.ID, "pwd").send_keys("admin")
# 7 | sendKeys | id=pwd | ${KEY_ENTER}
driver.find_element(By.ID, "pwd").send_keys(Keys.ENTER)
# 8 | click | css=.home-traffic > img | 
driver.find_element(By.CSS_SELECTOR, ".home-traffic > img").click()
# 9 | click | linkText=IP Filter | 
driver.find_element(By.LINK_TEXT, "IP Filter").click()
# 10 | click | id=filter00_ip | 
driver.find_element(By.ID, "filter00_ip").click()
# 11 | type | id=filter00_ip | 192.168.1.100
driver.find_element(By.ID, "filter00_ip").send_keys("192.168.1.100")
# 12 | click | id=to_submit | 
driver.find_element(By.ID, "to_submit").click()
# 13 | close |  | 
driver.close()
  
