# URL ==> https://tutorialsninja.com/demo/
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_products(self):

        self.driver.find_element(By.NAME,"search").send_keys("HP")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()


    def test_search_for_a_invalid_products(self):

        self.driver.find_element(By.NAME, "search").send_keys("QACircle")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_res='There is no product that matches the search criteria.'
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']//following-sibling::p").text.__eq__(expected_res)


    def test_search_for_a_without_providing_any_product_details(self):

        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_res = 'There is no product that matches the search criteria.'
        time.sleep(5)
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text.__eq__(expected_res)
