import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



IP_PAGE = "172.16.43.111"

def test_offset(test_expert):
    
    test_expert.go_to("//span[@id='btConfMetro']")
    test_expert.test_is_numeric("//input[@id='i1-Off']","a")  
    test_expert.test_is_numeric("//input[@id='i1-LowRange-ZerAdj']","b")
    test_expert.exit()


    

def test_duree(test_expert):
    test_expert.go_to("//span[@id='btConfCyc']")
    test_expert.test_is_numeric("//input[@id='St_CycZer-Dur']","zzzzz")  
    test_expert.exit()


def test_temperature(test_manager):
    test_manager.select_tab("//label[@id='lbButton2']")

    #test_manager.test_val_temperature(["//div[3]/table/tbody//input[@id='i0-LinCfA']",2],["//div[3]/table/tbody//input[@id='i0-LinCfB']",1],"//span[@id='analyseur-SEN0059']")

    test_manager.test_min("//input[@id='PWM_Pompe']","-1")
    test_manager.test_max("//input[@id='PWM_Pompe']","101")
