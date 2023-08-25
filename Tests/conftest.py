import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from configparser import ConfigParser


def read_conf(locator,value):
    config = ConfigParser()
    config.read('config.ini')
    return config.get(locator,value)

def capture_screenshot(driver,path):
    filename = path + "screenshot_" + str(time.asctime().replace(':',"_")) + ".png"
    driver.save_screenshot(filename)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def invoke_browser(request):
    browser = request.config.getoption("--browser_name")
    if browser == 'chrome':
        s = Service('D:\chrome116\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    driver.get('https://www.google.com')
    request.cls.driver = driver
    yield driver
    driver.close()