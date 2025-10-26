import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PYTEST.test.random_email_generate import generate_email

@pytest.mark.usefixtures("setup_and_teardown")

class TestRegister:
    def test_create_an_account_by_filling_all_mandatory_field(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//a[@title='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Basava")
        self.driver.find_element(By.ID, "input-lastname").send_keys("QACircle")
        self.driver.find_element(By.ID, "input-email").send_keys(generate_email())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("23456")
        self.driver.find_element(By.ID, "input-confirm").send_keys("23456")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        self.driver.implicitly_wait(10)
        exp_op="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(exp_op)



    def test_create_an_account_by_providing_all_field(self):
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Basava")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Gouda")
        self.driver.find_element(By.ID, "input-email").send_keys(generate_email())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("23456")
        self.driver.find_element(By.ID, "input-confirm").send_keys("23456")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        exp_op = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(exp_op)


