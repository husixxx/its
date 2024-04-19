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
    context.driver.find_element(By.LINK_TEXT, "Canon EOS 5D").click()

@then(u'Page with resulted product is displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Canon EOS 5D").text == "Canon EOS 5D"
    
### Scenario 4
@given(u'User is on "iPhone" product page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/iphone")
    
@when(u'User clicks on the related product')
def step_impl(context):

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)
    context.driver.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()

@then(u'Page of related product is displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'Apple Cinema 30"').text == 'Apple Cinema 30"'

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

# ### scenario 6
# @step(u'quantity of product is 0')
# def step_impl(context):
#     context.driver.find_element(By.ID, "input-quantity").clear()
#     context.driver.find_element(By.ID, "input-quantity").send_keys("0")
#     context.driver.find_element(By.ID, "button-cart").click()

### scenario 7
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
    context.driver.get("http://opencart:8080/en-gb/product/macbook")
    sleep(0.1)
    context.driver.find_element(By.ID, "button-cart").click()
    sleep(0.1)
    context.driver.get("http://opencart:8080")

@when(u'User click on the cart icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-cart-shopping").click()

@then(u'All the products in the cart are displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "MacBook").text == "MacBook" 