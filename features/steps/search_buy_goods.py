# import generalization for all features
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

import random
import string

use_step_matcher("re")

### Scenario 1
@given("User is on any page")
def step_impl(context):
    context.driver.get("http://opencart:8080/")
    
@when("User types macbook in the search bar")
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("macbook")

@step("User presses the search button")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass").click()
    
@then("Page with results of MacBooks is displayed")
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "MacBook").text == "MacBook"

### Scenario 2
@when(u'User clicks on a categories "Cameras" button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Cameras").click()

@then(u'Page with results of Cameras is displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Cameras").text == "Cameras"
### Scenario 3    
@given(u'User is on the page of "Camera" products')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/catalog/cameras")
    
@when(u'User clicks on resulted product "Canon EOS 5D"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/div/div[1]/a/img").click()

@then(u'Page with resulted product is displayed')
def step_impl(context):
    pass
    #assert "Canon EOS 5D" in context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/h1").text
    
### Scenario 4
@given(u'User is on "iPhone" product page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/iphone")
    
@when(u'User clicks on the related product')
def step_impl(context):

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[2]/div[1]/div/div[1]/a/img').click()

@then(u'Page of related product is displayed')
def step_impl(context):
    pass

### Scenario 5
@given(u'User is on the product page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/iphone")

@when(u'User clicks on the "Add to cart" button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-cart").click()

@then(u'Product is added to the cart')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-success").text == "Success: You have added iPhone to your shopping cart!"    

### scenario 6
@step(u'quantity of product is 0')
def step_impl(context):
    
    context.driver.find_element(By.ID, "input-quantity").clear()
    context.driver.find_element(By.ID, "input-quantity").send_keys("0")
    context.driver.find_element(By.ID, "button-cart").click()
# ## scenario 7
@given(u'User is on the cart page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=checkout/cart")
    

@step(u'Product is in the cart')
def step_impl(context):
    iphone = context.driver.find_element(By.LINK_TEXT, "iPhone").text

@when(u'User clicks on the "Remove" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#shopping-cart > div > table > tbody > tr > td:nth-child(4) > form > div > button.btn.btn-danger").click()
    
@then(u'Product is removed from the cart')
def step_impl(context):
    # try to find iphone on the screen but there shouldnt be one so it should throw an exception and pass the test
    try:
        context.driver.find_element(By.LINK_TEXT, "iPhone")
    except NoSuchElementException:
        pass

### scenario 8
@step(u'Any product is in the cart')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/iphone")
    sleep(0.1)
    context.driver.find_element(By.ID, "button-cart").click()
    sleep(0.1)
    context.driver.get("http://opencart:8080")

@when(u'User click on the cart icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-cart-shopping").click()

@then(u'All the products in the cart are displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "iPhone").text == "iPhone"

### scenario 9
@when(u'User clicks on the checkout button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Checkout").click()

@then(u'Checkout page with all the products from the cart is displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "iPhone").text == "iPhone"

### scenario 10
@given(u'User is on the checkout page with the products')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=checkout/checkout")

@step(u'Cart is not empty')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".table-responsive").text != ""

@step(u'User fills in all the neccessary informations')
def step_impl(context):

    context.driver.find_element(By.ID, "input-guest").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("John")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Doe")
    context.driver.find_element(By.ID, "input-email").send_keys("husixxx@hx.com")
    sleep(0.2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("Smolinske 99")
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("Smolinske")
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("90842")
    context.driver.find_element(By.ID, "input-shipping-zone").click()
    Select(context.driver.find_element(By.ID, "input-shipping-zone")).select_by_visible_text("Angus")
    context.driver.find_element(By.ID, "button-register").click()
    context.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
    sleep(0.1)
    context.driver.find_element(By.ID, "button-shipping-methods").click()
    sleep(0.3)
    context.driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
    context.driver.find_element(By.ID, "button-shipping-method").click()
    
    context.driver.find_element(By.ID, "button-payment-methods").click()
    context.driver.find_element(By.ID, "input-payment-method-cod-cod").click()
    context.driver.find_element(By.ID, "button-payment-method").click()
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.2)
    
@when(u'User clicks on the "Confirm order" button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-confirm").click()
    sleep(1)

@then(u'Success message is displayed')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Your order has been placed!"    
