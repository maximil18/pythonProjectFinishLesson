import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Feedback_page(Base):

    # Locators

    select_name = '//input[@name="fio"]'
    select_message = '//textarea[@name="notes"]'
    select_email = '//input[@name="email"]'

    # Getters

    def get_select_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_name)))

    def get_select_message(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_message)))

    def get_select_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_email)))


    # Actions

    def print_select_name(self):
        self.get_select_name().send_keys('Иванов Иван')
        print('Print name')

    def print_select_message(self):
        self.get_select_message().send_keys('Тестовое сообщение для проверки обратной связи')
        print('Print message')

    def print_select_email(self):
        self.get_select_email().send_keys('test@mail.ru')
        print('Print email')

    #Methods

    def print_information(self):
        self.get_current_url()
        time.sleep(1)
        self.print_select_name()
        time.sleep(1)
        self.print_select_message()
        time.sleep(1)
        self.print_select_email()
        time.sleep(1)
        self.get_screenshot()

