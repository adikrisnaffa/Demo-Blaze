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

@pytest.mark.next_slide
def test_next_slide(context):

    next_slide = context.find_element(By.XPATH, '//a[@data-slide="next"]')
    ActionChains(context).double_click(next_slide).perform()
    time.sleep(3)

@pytest.mark.prev_slide
def test_prev_slide(context):

    prev_slide = context.find_element(By.XPATH, '//a[@data-slide="prev"]')
    prev_slide.click()
    time.sleep(3)

@pytest.mark.categories
def test_categories(context):

    categories = context.find_element(By.ID, 'cat')
    categories.click()
    time.sleep(3)


@pytest.mark.phones
def test_phones(context):

    phones = context.find_element(By.XPATH, "//a[contains(text(),'Phones')]")
    phones.click()
    time.sleep(5)
    assert 'Samsung' in context.find_element(By.XPATH, '//div[@class="col-lg-4 col-md-6 mb-4"][1]').text

@pytest.mark.laptops
def test_laptops(context):

    laptops = context.find_element(By.XPATH, "//a[contains(text(),'Laptops')]")  
    laptops.click()
    time.sleep(5)
    assert 'MacBook air' in context.find_element(By.XPATH, '//div[@class="col-lg-4 col-md-6 mb-4"][3]').text

@pytest.mark.monitors
def test_monitors(context):

    monitors = context.find_element(By.XPATH, "//a[contains(text(),'Monitors')]")
    monitors.click()
    time.sleep(5)
    assert 'Apple monitor 24' in context.find_element(By.XPATH, '//div[@class="col-lg-4 col-md-6 mb-4"][1]').text