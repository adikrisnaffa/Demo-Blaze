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

@pytest.mark.contact
def test_contact(context):

    contact = context.find_element(By.XPATH, '//a[@data-target="#exampleModal"]')
    contact.click()
    WebDriverWait(context,10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-content"]')))
    assert 'New message' in context.find_element(By.ID, 'exampleModalLabel').text

    contact_email = context.find_element(By.ID, 'recipient-email')
    contact_email.send_keys('adikrisnanugraha@gmail.com')

    contact_name = context.find_element(By.ID, 'recipient-name')
    contact_name.send_keys('Adikrisna Nugraha')

    message = context.find_element(By.ID, 'message-text')
    message.send_keys('This is Test Automation with Selenemium Webdriver & Python Language')
    time.sleep(5)

    send_message = context.find_element(By.XPATH, '//button[@onclick="send()"]')
    send_message.click()
    time.sleep(3)

    alert = context.switch_to.alert
    alert.accept()

@pytest.mark.about_us
def test_about_us(context):

    about_us = context.find_element(By.XPATH, '//a[@data-target="#videoModal"]')
    about_us.click()
    time.sleep(3)
    assert 'About us' in context.find_element(By.ID, 'videoModalLabel').text

    play_video = context.find_element(By.XPATH, '//button[@title="Play Video"]')
    play_video.click()
    time.sleep(3)
