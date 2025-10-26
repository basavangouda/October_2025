from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestLogin:

    def test_login_chrome(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        self.product=self.driver.find_element(By.XPATH,"//span[text()='Products']").text
        assert self.product=="Products"

        self.driver.close()

    def test_login_edge(self):
        self.driver=webdriver.Edge()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        self.product = self.driver.find_element(By.XPATH, "//span[text()='Products']").text
        assert self.product == "Products"

        self.driver.close()

    def test_login_firefox(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        self.product = self.driver.find_element(By.XPATH, "//span[text()='Products']").text
        assert self.product == "Products"

        self.driver.close()

