#Selenium Webdriver must be installed for this to work

import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 1

#youtube link
link = 'https://youtu.be/dPHnV2Lo2n0'

#number of views
views = 63

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
