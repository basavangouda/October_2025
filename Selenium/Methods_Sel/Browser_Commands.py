from selenium import webdriver
from selenium.webdriver.common.by import By
import time



#Example 1
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.close()

#Example 2
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.firstcry.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Track Order']").click()
time.sleep(10)
driver.quit()
time.sleep(10)





