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

@pytest.mark.add_item_product
def test_add_item_product(context):

    add_item_product = context.find_element(By.XPATH, '//div[@class="col-lg-4 col-md-6 mb-4"][1]//div[@class="card h-100"]//img[@class="card-img-top img-fluid"]')
    add_item_product.click()
    time.sleep(3)
    context.find_element(By.XPATH, '//a[@onclick="addToCart(1)"]').click()
    time.sleep(5)
    alert = context.switch_to.alert
    alert.accept()
    time.sleep(5)

    
    cart = context.find_element(By.ID, 'cartur')
    cart.click()
    time.sleep(3)
    assert 'https://www.demoblaze.com/cart.html' in context.current_url

    place_order = context.find_element(By.XPATH, '//button[@data-target="#orderModal"]')
    place_order.click()

    name = context.find_element(By.ID, 'name')
    name.send_keys('Test Name')

    country = context.find_element(By.ID, 'country')
    country.send_keys('Test Country')

    city = context.find_element(By.ID, 'city')
    city.send_keys('Test City')

    credit_card = context.find_element(By.ID, 'card')
    credit_card.send_keys('Test Credit Card')

    month = context.find_element(By.ID, 'month')
    month.send_keys('Test Month')

    year = context.find_element(By.ID, 'year')
    year.send_keys('Test Year')
    time.sleep(5)


    purchase = context.find_element(By.XPATH, '//button[@onclick="purchaseOrder()"]')
    purchase.click()
  
    context.find_element(By.XPATH, '//button[@tabindex="1"]').click()
    time.sleep(3)
