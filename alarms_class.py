import pytest
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep


class TestAlarms():

    def __init__(self,alarm_page,ip_page):
        self.page = alarm_page    
        self.ip = ip_page

    def get_name():
        return "Alarms"
    

    def select_tab(self,element):
        tab = WebDriverWait(self.page,10).until(EC.visibility_of_element_located((By.XPATH,element)))    
        tab.click()
        
