import os
import subprocess
import time
import json
import xml.etree.ElementTree as ET
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#driver = webdriver.Chrome('/home/adit/Downloads/chromedriver')



# 1 | open | http://modem.wifi/mark_set_mac.w.xml?_=1593627509977 | 
#driver.get("http://modem.wifi/mark_set_mac.w.xml?_="+str(int(round(time.time()*1000))))
# 2 | setWindowSize | 683x741 | 
#driver.set_window_size(683, 741)

#requests.get("http://modem.wifi/mark_set_mac.w.xml?_="+str(int(round(time.time()*1000))))

#tree = ET.parse('http://modem.wifi/mark_set_mac.w.xml?_='+str(int(round(time.time()*1000))))

xmlfile = requests.get("http://modem.wifi/mark_set_mac.w.xml?_="+str(int(round(time.time()*1000))))

print(xmlfile.text)

check = re.search("unknown(static ip)", xmlfile.text)

print(check)

if check == None:
	check = "no"

if check == "no":
	print("There is no intrusion")
else:
	print("intrusion possibility")

subprocess.call(['bash','./script_start.sh',check])


#mytree = ET.parse('xmlfile')

#myroot = mytree.getroot()

#print(myroot[2])

#for i in range(10): 
#	for x in myroot[2][i]:
#		if x.text == "unknown(static ip)":
#			print("intrusion possibility")		
#		print(x.text)
    
