import pytest
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep
from main import IP_PAGE
from manager_class import TestManager
from alarms_class import TestAlarms
from expert_class import TestExpert

@pytest.fixture(scope="session")
def manager_page():
        driver = webdriver.Firefox()
        URL_PAGE="http://" + IP_PAGE + "/analyser/configuration.html"
        
        driver.get(URL_PAGE)
        WebDriverWait(driver,10).until(lambda dr:dr.execute_script("return document.readyState") == "complete")
        passwordIhm = driver.find_element(By.XPATH, "//input[@id='idPass']")
        passwordIhm.clear()
        passwordIhm.send_keys("aS20Ven15")

        buttonValidate = driver.find_element(By.ID, "btValidPass")
        buttonValidate.click()

        yield driver

        driver.quit()


@pytest.fixture(scope="session")
def alarms_page():
        driver = webdriver.Firefox()
        URL_PAGE="http://" + IP_PAGE + "/cfg_deep/EventsCfg.html"
        
        driver.get(URL_PAGE)
        WebDriverWait(driver,10).until(lambda dr:dr.execute_script("return document.readyState") == "complete")
        passwordIhm = driver.find_element(By.XPATH, "//input[@id='idPass']")
        passwordIhm.clear()
        passwordIhm.send_keys("aS20Ven15")

        buttonValidate = driver.find_element(By.ID, "btValidPass")
        buttonValidate.click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='btValid']")))

        yield driver

        driver.quit()


@pytest.fixture(scope="session")
def expert_page():
        driver = webdriver.Firefox()
        URL_PAGE="http://" + IP_PAGE
        driver.get(URL_PAGE)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='idPass']")))
        current_url = driver.current_url
        passwordIhm = driver.find_element(By.XPATH, "//input[@id='idPass']")
        passwordIhm.clear()
        passwordIhm.send_keys("00007")
        print(f"Current URL before waiting: {current_url}")
        buttonValidate = driver.find_element(By.ID, "btValidPass")
        buttonValidate.click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//iframe[@id='ifrAct']")))
        driver.switch_to.frame('ifrAct')

        buttonMenu = driver.find_element(By.XPATH, "//span[@id='btMaint']")
        buttonMenu.click()
        driver.switch_to.default_content()
        WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ifrMain")))

        yield driver

        driver.quit()


@pytest.fixture
def test_manager(manager_page):

    return TestManager(manager_page,IP_PAGE)

@pytest.fixture
def test_alarms(alarms_page):
    return TestAlarms(alarms_page,IP_PAGE)

@pytest.fixture
def test_expert(expert_page):
    return TestExpert(expert_page,IP_PAGE)
