#expert_class.py

import pytest
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep


class TestExpert():

    def __init__(self,expert_page,ip_page):
        self.page = expert_page    
        self.ip = ip_page

    def get_name():
        return "Expert"
    
    
    def go_to(self,xpath):
        WebDriverWait(self.page,10).until(EC.visibility_of_element_located(
        (By.XPATH, xpath)))
        buttonPass = self.page.find_element(By.XPATH,xpath)
        buttonPass.click()
        buttonGo = self.page.find_element(By.XPATH,"//span[@id='btGo']")
        buttonGo.click()

    def exit(self):
        sleep(0.5)
        backButton = WebDriverWait(self.page,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='btGoBack']"))) 
        backButton.click()

        
    def test_is_numeric (self, xpath, value):

        offset = WebDriverWait(self.page,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
        offset.click()
        offsetValue = offset.get_attribute("name")
        for _ in range(len(offsetValue)):
           offset.send_keys(Keys.BACKSPACE)
        #offset.clear()    
        offset.send_keys(value)
        
        valid = WebDriverWait(self.page,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='btValid']")))
        valid.click()
        offsetValue = offset.get_attribute("name")
        
        assert offsetValue.isdigit() == True
