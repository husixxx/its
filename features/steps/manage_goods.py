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
from selenium.webdriver.common.alert import Alert

import random
import string
use_step_matcher("re")

### scenario 11
@given(u'User is logged as an admin')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/")
    sleep(0.1)
    context.driver.find_element(By.ID,"input-username").send_keys("user")
    context.driver.find_element(By.ID,"input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary").click()
    sleep(1)
@when(u'User is on any admin page')
def step_impl(context):
    pass
@step(u'User clicks on the "Products" tab')
def step_impl(context):
    # context.driver.find_element(By.CSS_SELECTOR, "i.fa-solid.fa-bars").click()
    # sleep(0.1)
    context.driver.find_element(By.CSS_SELECTOR, "a.parent.collapsed").click()
    sleep(0.1)
    context.driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[2]/ul/li[2]/a").click()

    sleep(1)

@then(u'Page with list of goods is displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/h1").text == "Products"

### scenario 12
@step(u'User is on the "Products" tab')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "a.parent.collapsed").click()
    sleep(0.1)
    context.driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[2]/ul/li[2]/a").click()
    sleep(0.1)
   
@step(u'User clicks on the "Add New" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/a/i").click()
    sleep(1)
@step(u'User fills in all neccessary details')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name-1").send_keys("Test product")
    # generate random string
    letters = string.ascii_lowercase
    random_str = ''.join(random.choice(letters) for i in range(10))

    context.driver.find_element(By.ID, "input-meta-title-1").send_keys(random_str)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[2]/a").click()
    sleep(0.2)
    random_str = ''.join(random.choice(letters) for i in range(10))
    context.driver.find_element(By.ID, "input-model").send_keys(random_str)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[11]/a").click()
    random_str = ''.join(random.choice(letters) for i in range(10))
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys(random_str)

@step(u'User clicks on the "Save" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/button").click()
    sleep(0.1)

@then(u'Product is created and success message is displayed')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-success").text == "Success: You have modified products!"

### scenario 13
@when(u'User clicks on the checkbox of product to be deleted')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[1]/input").click()
    sleep(0.1)
    
@step(u'User clicks on the "Delete" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/button[3]").click()
    sleep(0.1)
    Alert(context.driver).accept()
    sleep(0.1)
@then(u'The product is deleted and success message is displayed')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-success").text == "Success: You have modified products!"

### scenario 14
@when(u'User clicks on the "Edit" button of the product to be updated')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[7]/div/a/i").click()
    sleep(1)

@step(u'User changes the product')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name-1").send_keys("Test product")
    # generate random string
    letters = string.ascii_lowercase
    random_str = ''.join(random.choice(letters) for i in range(10))

    context.driver.find_element(By.ID, "input-meta-title-1").send_keys(random_str)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[2]/a").click()
    sleep(0.2)
    random_str = ''.join(random.choice(letters) for i in range(10))
    context.driver.find_element(By.ID, "input-model").send_keys(random_str)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[11]/a").click()
    random_str = ''.join(random.choice(letters) for i in range(10))
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys(random_str)

@then(u'The product is updated and success message is displayed')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-success").text == "Success: You have modified products!"

### scenario 15
@step(u'Products quantity is not zero')
def step_impl(context):
    pass
    # assert context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[6]/span").text != "0"

@step(u'User changes the products quantity')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name-1").send_keys("Test product")
    # generate random string
    letters = string.ascii_lowercase
    random_str = ''.join(random.choice(letters) for i in range(10))

    context.driver.find_element(By.ID, "input-meta-title-1").send_keys(random_str)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[2]/a").click()
    sleep(0.1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.1)
    context.driver.find_element(By.ID, "input-quantity").clear()
    context.driver.find_element(By.ID, "input-quantity").send_keys("5")
    context.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[2]/a").click()
    sleep(0.2)
    random_str = ''.join(random.choice(letters) for i in range(10))
    context.driver.find_element(By.ID, "input-model").send_keys(random_str)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[11]/a").click()
    random_str = ''.join(random.choice(letters) for i in range(10))
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys(random_str)

@then(u'The products quantity is updated and success message is displayed')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-success").text == "Success: You have modified products!"

