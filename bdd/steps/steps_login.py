from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@given('I open the login page')
def open_login(context):

    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Firefox(service=service, options=options)
    context.driver.maximize_window()
    context.driver.get('https://www.saucedemo.com')
    

@when('I login with "{user}" and "{password}"')
def do_login(context, user, password):
    context.driver.find_element("id",'user-name').send_keys(user)
    context.driver.find_element("id",'password').send_keys(password)
    context.driver.find_element("id",'login-button').click()

@then('I should see the inventory page')
def see_inventory(context):
    assert 'inventory' in context.driver.current_url