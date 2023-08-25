import logging

import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import time
import sys
from conftest import read_conf,capture_screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from  logger import Logger
@pytest.mark.usefixtures('invoke_browser')
class Base:
    pass

log = Logger(__name__,logging.INFO)

class TestUI(Base):

    five_star_li = []

    def test_verify_google(self):
        log.logger.info('Launching chrome browser and generating log')
        self.driver.get(read_conf('urls','google'))
        title = self.driver.title
        log.logger.info('taking the page title to verify')
        print(title)
        assert title == read_conf('titles','google_home')
        log.logger.info('title verified successfully')

    def test_enter_search_amazon(self):
        self.driver.find_element(By.XPATH,read_conf('locators','google_search')).send_keys('amazon.in')
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,read_conf('locators','google_button')).click()
        title = self.driver.title
        print(title)
        assert title == read_conf('titles','google_search_amazon')

    def test_print_all_test_results(self):
        links = self.driver.find_elements(By.TAG_NAME,'a')
        for link in links:
            print(link.text)

    def test_click_amazon(self):
        self.driver.get(read_conf('urls','amazon'))
        title = self.driver.title
        capture_screenshot(self.driver,'../Screenshots/')
        assert title == read_conf('titles','amazon_home')

    def test_signin_amazon(self):
        actions = ActionChains(self.driver)
        ele = self.driver.find_element(By.XPATH,read_conf('locators','amazon_sign'))
        actions.move_to_element(ele)
        self.driver.implicitly_wait(3)
        element = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,read_conf('locators','sign_in'))))
        #element.click()
        title = self.driver.title
        print(title)
        #assert title == read_conf('titles','amazon_sign_in')

    # def test_login(self):
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(By.XPATH,read_conf('login','username')).sendkeys('7658962143')
    #     self.driver.find_element(By.XPATH, read_conf('login', 'continue')).click()
    #     self.driver.find_element(By.XPATH, read_conf('login', 'password')).sendkeys('trinadh@345')
    #     self.driver.find_element(By.XPATH,read_conf('login','signin')).click()


    def test_click_all_electronics(self):
        dropdown = self.driver.find_element(By.XPATH,read_conf('locators','am_all'))
        select = Select(dropdown)
        select.select_by_visible_text('Electronics')
        time.sleep(3)

    def test_search_dell(self):
        self.driver.find_element(By.XPATH,read_conf('locators','am_search_input')).send_keys("dell")
        self.driver.find_element(By.XPATH,read_conf('locators','am_search_button')).click()
        items = self.driver.find_elements(By.XPATH,read_conf('locators','am_dell_items'))
        for item in items:
            print(item.text)

    def test_apply_filter(self):
        self.driver.find_element(By.XPATH,read_conf('locators','filter_min')).send_keys('30000')
        self.driver.find_element(By.XPATH, read_conf('locators', 'filter_max')).send_keys('50000')
        self.driver.find_element(By.XPATH,read_conf('locators','filter_button')).click()

    def test_five_star(self):
        items = self.driver.find_elements(By.XPATH,read_conf('locators','five_star'))
        for item in items:
            print(item.text)
        print(items)

    def test_creating_wishlist(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        actions = ActionChains(self.driver)
        ele = self.driver.find_element(By.XPATH,read_conf('locators','amazon_sign'))
        actions.move_to_element(ele).click()
        self.driver.find_element(By.XPATH,read_conf('locators','wish_list')).click()

