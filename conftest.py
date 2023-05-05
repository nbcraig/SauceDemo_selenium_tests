import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from datetime import datetime

@pytest.fixture
def driver():
    url = "https://saucedemo.com"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.close()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = './reports/html_reports/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"