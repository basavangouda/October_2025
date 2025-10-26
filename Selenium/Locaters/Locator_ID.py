from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Example 1
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.close()

#Example 2
driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
driver.maximize_window()
print(driver.find_element(By.ID,"category").text)
driver.close()