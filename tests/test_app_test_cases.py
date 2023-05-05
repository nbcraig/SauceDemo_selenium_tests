import pytest
from selenium.common.exceptions import NoSuchElementException
from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_valid_login(driver):
    instance = LoginPage(driver)
    instance.login('standard_user', 'secret_sauce')
    try:
        instance.check_successful_login()
        assert True
    except NoSuchElementException:
        assert False

def test_error_message_on_invalid_login(driver):
    instance = LoginPage(driver)
    instance.login('not_username', 'not_password')
    try:
        instance.check_error_message()
        assert True
    except NoSuchElementException:
        assert False

def test_logout(driver):
    login_instance = LoginPage(driver)
    instance = HomePage(driver)

    login_instance.login('standard_user', 'secret_sauce')
    instance.logout()
    try:
        login_instance.check_successful_login()
        assert False
    except NoSuchElementException:
        assert True

def test_sort_price_low_to_high(driver):
    login_instance = LoginPage(driver)
    instance = HomePage(driver)
    login_instance.login('standard_user', 'secret_sauce')
    instance.sort_low_to_high()
    # Check if prices are sorted
    price_list = instance.get_inventory_prices_list()
    assert price_list == sorted(price_list)

def test_add_multiple_items_to_cart(driver):
    login_instance = LoginPage(driver)
    instance = HomePage(driver)
    login_instance.login('standard_user', 'secret_sauce')
    instance.add_to_cart()
    inventory_items_titles = instance.inventory_items_titles()
    cart_titles = instance.cart_titles()
    assert inventory_items_titles == cart_titles

def test_add_specific_item_to_cart(driver):
    login_instance = LoginPage(driver)
    instance = HomePage(driver)
    login_instance.login('standard_user', 'secret_sauce')
    instance.add_specific_item_to_cart('add-to-cart-sauce-labs-onesie')
    cart_titles = instance.cart_titles()
    assert cart_titles == ['Sauce Labs Onesie']

def test_check_out(driver):
    login_instance = LoginPage(driver)
    instance = HomePage(driver)
    login_instance.login('standard_user', 'secret_sauce')
    instance.add_to_cart()
    instance.complete_purchase()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'