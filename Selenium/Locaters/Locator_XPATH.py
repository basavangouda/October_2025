from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# #Absolute Xpath
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://qacircle.com/")
# text=driver.find_element(By.XPATH,"/html/body/nav/div[2]/div/div[3]/ul/li[3]/a").text
# print(text)
# time.sleep(5)
# driver.close()
#
# #Relative Xpath
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.nykaa.com/")
# text=driver.find_element(By.XPATH,"//button[@class='css-1gzc5zn']").text
# print(text)
# time.sleep(5)
# driver.close()

#example 1 contains()
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.find_element(By.XPATH,"//input[contains(@name,'emp_name')]").send_keys("Good Morning")
# time.sleep(5)
# driver.close()

"""
//*[contains(@id,'id value')]

//*[contains(@href,'url')]

//*[contains(@type,'value')]

//*[contains(@src,'imagelink')]

"""
#example 2 text()
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.firstcry.com/")
# driver.find_element(By.XPATH,"//span[text()='Track Order']").click()
# time.sleep(5)
# driver.close()

#example 3 partial text() and Contains
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.firstcry.com/")
# driver.find_element(By.XPATH,"//span[contains(text(),' Regi')]").click()
# time.sleep(5)
# driver.close()

#XPath using AND /OR Conditions
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH,"//input[@data-test='username' and @type='text']").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='texttyr' or @type='password']").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(5)
driver.close()
