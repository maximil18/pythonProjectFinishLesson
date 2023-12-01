import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Person_information_page(Base):


    # Locators

    select_no_registr = '//a[@href="/account/quickprofile?returnUrl=%2Forder%2Fform%3Ffrom%3Dcart"]'
    select_button_person = '//label[@data-value="03.01"]'
    select_last_name = '//input[@id="lastname"]'
    select_first_name = '//input[@id="firstname"]'
    select_email = '//input[@id="email"]'
    select_phone = '//input[@id="phone"]'



    # Getters

    def get_select_no_registr(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_no_registr)))

    def get_select_button_person(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_button_person)))

    def get_select_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_last_name)))

    def get_select_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_first_name)))

    def get_select_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_email)))

    def get_select_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_phone)))

    # Actions

    def click_select_no_registr(self):
        self.get_select_no_registr().click()
        print('Click select no registr')

    def click_select_button_person(self):
        self.get_select_button_person().click()
        print('Click select button person')

    def print_select_last_name(self):
        self.get_select_last_name().send_keys('Иванов')
        print('Print last name')

    def print_select_first_name(self):
        self.get_select_first_name().send_keys('Иван')
        print('Print first name')

    def print_select_email(self):
        self.get_select_email().send_keys('test@mail.ru')
        print('Print email')

    def print_select_phone(self):
        self.get_select_phone().send_keys('88005553535')
        print('Print phone')

    #Methods

    def print_person_information(self):

        self.click_select_no_registr()
        time.sleep(1)
        self.click_select_button_person()
        time.sleep(1)
        self.print_select_last_name()
        time.sleep(1)
        self.print_select_first_name()
        time.sleep(1)
        self.print_select_email()
        time.sleep(1)
        self.print_select_phone()
        time.sleep(1)
        self.get_screenshot()













