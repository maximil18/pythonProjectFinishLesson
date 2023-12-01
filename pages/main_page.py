import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    url = 'https://www.chipdip.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_catalog = '//button[@class="header__button header__catalog-button"]'
    select_category = '//a[@href="/catalog/electronics-equipment"]'
    select_tablet_devices = '//a[@href="/catalog-show/tablet-devices"]'
    select_feedback_button = '//a[@href="/forms/feedback"]'
    select_calculator = '//a[@href="/calc"]'

    # Getters

    def get_select_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_catalog)))

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_category)))

    def get_select_tablet_devices(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_tablet_devices)))

    def get_select_feedback_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_feedback_button)))

    def get_select_calculator(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_calculator)))


    # Actions

    def click_select_catalog(self):
        self.get_select_catalog().click()
        print('Click select catalog')

    def click_select_category(self):
        self.get_select_category().click()
        print('Click select category')

    def click_select_tablet_devices(self):
        self.get_select_tablet_devices().click()
        print('Click select tablet devices')

    def click_select_feedback_button(self):
        self.get_select_feedback_button().click()
        print('Click select feedback button')

    def click_select_calculator(self):
        self.get_select_calculator().click()
        print('Click select calculator')


    #Methods

    def select_category_products(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(1)
        self.click_select_catalog()
        time.sleep(1)
        self.click_select_category()
        time.sleep(1)
        self.click_select_tablet_devices()
        self.assert_url('https://www.chipdip.ru/catalog-show/tablet-devices')

    def feedback_check(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(1)
        self.click_select_feedback_button()
        time.sleep(1)
        self.assert_url('https://www.chipdip.ru/forms/feedback')

    def calculator_check(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(1)
        self.click_select_calculator()
        time.sleep(1)
        self.assert_url('https://www.chipdip.ru/calc')



