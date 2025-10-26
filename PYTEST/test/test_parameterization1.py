import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSwagLab:

    @pytest.fixture()
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("locked_out_user","secret_sauce"),("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce"),("error_user","secret_sauce"),("visual_user","secret_sauce")])
    def test_swaglab_login_page(self,username,password):
       self.driver=webdriver.Chrome()
       self.driver.get("https://www.saucedemo.com/")
       self.driver.find_element(By.ID,"user-name").send_keys(username)
       self.driver.find_element(By.ID,"password").send_keys(password)
       time.sleep(5)
       self.driver.find_element(By.ID,"login-button").click()
       time.sleep(5)
       try:
           self.status=self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").is_displayed()
           assert self.status==True
           self.driver.close()

       except:
           self.driver.close()
           assert self.status==False