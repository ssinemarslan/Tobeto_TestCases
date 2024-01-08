# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

class TestTestcase1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testcase1(self):
    self.driver.get("https://tobeto.com/giris")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.NAME, "email").click()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "email")))
    self.driver.find_element(By.NAME, "email").send_keys("sinemarslantr@gmail.com")
    self.driver.find_element(By.NAME, "password").click()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "password")))
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("r4jS2QvfZpn8fZd")
    self.driver.find_element(By.XPATH, "//button[contains(.,'Giriş Yap')]").click()
    
    WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='toast-body']")))
    assert self.driver.find_element(By.XPATH,"//div[@class='toast-body']").text == "• Giriş başarılı."

  
   
  
