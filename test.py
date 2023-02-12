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

@pytest.mark.cart
def test_cart(context):

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

    phones = context.find_element(By.XPATH, '//a[@onclick=\"byCat(\"phone\")\"]')
    phones.click()
    time.sleep(3)

@pytest.mark.laptops
def test_laptops(context):

    laptops = context.find_element(By.CSS_SELECTOR, "a[@onclick=\"byCat(\"notebook\")\"]")  
    laptops.click()
    time.sleep(3)

@pytest.mark.monitors
def test_monitors(context):

    monitors = context.find_element(By.XPATH, '')
    monitors.click()
    time.sleep(3)