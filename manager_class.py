#manager_class.py

import pytest
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep


    


class TestManager():

    def __init__(self,manager_page,ip_page):
        self.page = manager_page    
        self.ip = ip_page

    def get_name():
        return "Manager"
    
    
    def first_occurence(self, datajs, alarmIndex):
        found = {index: None for index in alarmIndex}
        for object in datajs:
            index = object['index']
            if index in found and found[index] is None:
                found[index] = {'start': object['start'], 'stop': object['stop'], 'value': object['val']}

                if all(value is not None for value in found.values()):
                    break     
        return found

    
    def get_temp_alarms(self):
        url_requete = "http://"+self.ip+ "/cgi-bin/cgi_getalarms"
        print(f"{url_requete}")
        request_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
                          "Accept": "application/json, text/javascript, */*; q=0.01",
                          "Referer": "http://"+self.get_ip()+"/desktop/diagnostic.html"}
        tempValueResponse = requests.get(url_requete,headers=request_header)

        if tempValueResponse.status_code == 200:
            tempValueJson = tempValueResponse.json()['data']
        else:
            print(f"erreur de recuperation du JSON : {tempValueResponse.status_code}")

        alarms = ['A32','A34']
        alarmsValues = self.first_occurence(tempValueJson,alarms)
        print(f"{alarmsValues}")
        return alarmsValues

    def run_tests(self):

        exit_manager = pytest.main(["tests_manager/", "-v", "--disable-warnings", "--tb=native"])
    
        if exit_manager != 0:
            print(f"Tests in manager level failed with exit code : {exit_manager}")       # "/html/body/div[2]/div[2]/div/div[2]/div[3]/table/tbody//input[@id='i1-LinCfA']"
        
        return exit_manager
    
    def select_tab(self,xpath):
        WebDriverWait(self.page,10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "ifrConf")))
    
        buttTemp = WebDriverWait(self.page,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))    
        buttTemp.click()
        sleep(1)
    
    def set_coefA_temperature(self,xpath,valA):
        
        tempA = WebDriverWait(self.page,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        tempAname = tempA.get_attribute("name")
        for _ in range(len(tempAname)):
            tempA.send_keys(Keys.BACKSPACE)
        tempA.send_keys(valA)
        buttonValidate = self.page.find_element(By.ID, "btValid")
        buttonValidate.click()

    def set_coefB_temperature(self,xpath,valB):
        
        tempB = WebDriverWait(self.page,10).until(EC.presence_of_element_located((By.XPATH,xpath)))       #"/html/body/div[2]/div[2]/div/div[2]/div[3]/table/tbody//input[@id='i1-LinCfB']"
        tempBname = tempB.get_attribute("name")
        for _ in range(len(tempBname)):
            tempB.send_keys(Keys.BACKSPACE)
        tempB.send_keys(valB)
        buttonValidate = self.page.find_element(By.ID, "btValid")
        buttonValidate.click()

    def get_temperature(self,xpath):
       
        tempValue=self.page.find_element(By.XPATH,xpath).text
        return tempValue


    def get_coefA_temperature(self,xpath):
      
        tempA = WebDriverWait(self.page,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        valTempA = tempA.get_attribute("name")
        return valTempA

    def get_coefB_temperature(self,xpath):
        
        tempB = WebDriverWait(self.page,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        valTempB = tempB.get_attribute("name")
        return valTempB
    
    def quit(self,driver):
        driver.quit()

    def test_val_temperature(self,A,B,temperature):
        addressA = A[0]
        addressB = B[0]
        valA = A[1]
        valB = B[1]
        initialA = self.get_coefA_temperature(addressA)
        initialB = self.get_coefB_temperature(addressB)
        initialTemp = self.get_temperature(temperature).split(' ')[0]
        self.set_coefA_temperature(addressA,valA)
        self.set_coefB_temperature(addressB,valB)
        sleep(2)
        newValTemp = self.get_temperature(temperature).split(' ')[0]
        
        assert abs(float(newValTemp) - (float(valA) * ((float(initialTemp)-float(initialB))/float(initialA)) + float(valB))) <0
    

    
    def test_is_numeric (self, xpath, value):

        element = WebDriverWait(self.page,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
        element.click()
        elementValue = element.get_attribute("name")
        for _ in range(len(elementValue)):
            element.send_keys(Keys.BACKSPACE)
          
        element.send_keys(value)
        
        valid = WebDriverWait(self.page,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='btValid']")))
        valid.click()
        elementValue = element.get_attribute("name")
        
        assert elementValue.isdigit() == True

    def test_min(self,xpath,value):
        element = WebDriverWait(self.page,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
        element.click()
        sleep(1)
        min_limit = element.get_attribute("min")
        elementValue = element.get_attribute("name")
        #for _ in range(len(elementValue)):
         #   element.send_keys(Keys.BACKSPACE)
        element.clear() 
        sleep(1)  
        element.send_keys(value)
        sleep(1) 
        valid = WebDriverWait(self.page,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='btValid']")))
        valid.click()
        elementValue = element.get_attribute("name")

        assert float(elementValue) >= float(min_limit)

    def test_max(self,xpath,value):
        element = WebDriverWait(self.page,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
        element.click()
        sleep(1)
        max_limit = element.get_attribute("max")
        elementValue = element.get_attribute("name")
        #for _ in range(len(elementValue)):
        #    element.send_keys(Keys.BACKSPACE)
        element.clear()
        sleep(1)
        element.send_keys(value)
        sleep(1) 
        valid = WebDriverWait(self.page,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='btValid']")))
        valid.click()
        elementValue = element.get_attribute("name")

        assert float(elementValue) >= float(max_limit)
