import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

import time
def pytest_addoption(parser):
   parser.addoption("--browser")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
   outcome = yield
   rep = outcome.get_result()
   setattr(item, "rep_" + rep.when, rep)
   return rep


@pytest.fixture()
def log_on_failure(request):
   msgs = []
   yield
   item = request.node
   if item.rep_call.failed:
      allure.attach(driver.get_screenshot_as_png(), name="Failed Test Cases",
                    attachment_type=AttachmentType.PNG)


@pytest.fixture()
def setup_and_teardown(request):
  #make drive as global, Otherwise we will get problem
  global driver
  browser=request.config.getoption("--browser")
  if browser =="chrome":
      driver = webdriver.Chrome()
  elif browser  == "firefox":
      driver = webdriver.Firefox()
  elif browser  == "edge":
      driver = webdriver.Edge()
  else:
      print("Please enter the valid browser")


  driver.get("https://tutorialsninja.com/demo/")
  driver.maximize_window()
  request.cls.driver = driver
  yield
  driver.quit()
