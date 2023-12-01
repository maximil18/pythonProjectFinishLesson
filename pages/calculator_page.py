import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Calculator_page(Base):

    # Locators

    select_capacitor = '//a[@href="/calc/capacitor"]'
    select_entered_data = '//input[@id="cap_value"]'
    select_output_data_1 = '//td[@id="f_row1_val"]'
    select_output_data_2 = '//td[@id="f_row2_val"]'


    # Getters

    def get_select_capacitor(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_capacitor)))

    def get_entered_data(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_entered_data)))

    def get_select_output_data_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_output_data_1)))

    def get_select_output_data_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_output_data_2)))


    # Actions

    def clock_select_capacitor(self):
        self.get_select_capacitor().click()
        print('Click capacitor')

    def print_entered_data(self):
        self.get_entered_data().send_keys('10')
        print('Print entered data')

    def return_select_output_data_1(self):
        output_data_1 = self.get_select_output_data_1().text
        return output_data_1

    def return_select_output_data_2(self):
        output_data_2 = self.get_select_output_data_2().text
        return output_data_2

    #Methods

    def check_capacitor_calculator(self):
        self.get_current_url()
        time.sleep(1)
        self.clock_select_capacitor()
        time.sleep(1)
        self.print_entered_data()
        time.sleep(1)
        assert self.return_select_output_data_1() == '0.01'
        print('Первая величина переведена верно')
        assert self.return_select_output_data_2() == '10000'
        print('Вторая величина переведена верно')
        self.get_screenshot()

