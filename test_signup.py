from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/index.html")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.signup
def test_signup(context):

    signup = context.find_element(By.ID, 'signin2')
    signup.click()
    
    username = context.find_element(By.ID, 'sign-username')
    username.send_keys('1212121212')
    time.sleep(3)

    password = context.find_element(By.ID, 'sign-password')
    password.send_keys('12345')
    time.sleep(3)

    click_signup = context.find_element(By.XPATH, "//button[contains(text(), 'Sign up')]")
    click_signup.click()
    time.sleep(3)

    alert = context.switch_to.alert
    alert.accept()


@pytest.mark.login_logout
def test_login_logout(context):

    login = context.find_element(By.XPATH, '//a[@data-target="#logInModal"]')
    login.click()
    
    username = context.find_element(By.ID, 'loginusername')
    username.send_keys('1212121212')

    password = context.find_element(By.ID, 'loginpassword')
    password.send_keys('12345')
    time.sleep(2)

    click_login = context.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
    click_login.click()
    time.sleep(5)
    assert '1212121212' in context.find_element(By.ID, 'nameofuser').text

    logout = context.find_element(By.ID, 'logout2')
    logout.click()
    time.sleep(3)
    assert 'Log in' in context.find_element(By.XPATH, '//a[@data-target="#logInModal"]').text
    