import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_page(Base):


    # Locators

    select_product_1_name_cart = '//a[@href="/product0/8025849556"]'
    select_product_2_name_cart = '//a[@href="/product0/8025849471"]'
    select_all_price = '//span[@class="price"]'
    select_delete_product_2 = '//button[@data-id="8025849471"]'
    select_add_product_1 = '//*[@id="cart"]/tbody[1]/tr[1]/td[5]/button[2]'
    text_delivery = '//*[@id="cart"]/tbody[2]/tr[1]/td[4]/div[3]'
    button_placing = '//button[@class="button button_big button_w100 not-print"]'

    # Getters

    def get_select_product_1_name_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1_name_cart)))

    def get_select_product_2_name_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_2_name_cart)))

    def get_select_all_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_all_price)))

    def get_select_delete_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_delete_product_2)))

    def get_select_add_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_add_product_1)))

    def get_text_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.text_delivery)))

    def get_button_placing(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_placing)))

    # Actions

    def save_select_product_1_name_cart(self):

        product_1_name_in_cart = self.get_select_product_1_name_cart().text
        return product_1_name_in_cart

    def save_select_product_2_name_cart(self):

        product_2_name_in_cart = self.get_select_product_2_name_cart().text
        return product_2_name_in_cart

    def save_all_price_in_cart(self):

        price_in_cart = self.get_select_all_price().text
        return int(price_in_cart.replace(' ', ''))

    def click_select_delete_product_2(self):
        self.get_text_delivery().click()
        self.get_select_delete_product_2().click()
        print('Click delete product 2')

    def click_add_product_1(self):
        self.get_select_add_product_1().click()
        print('Click add product 1')

    def click_button_placing(self):
        self.get_button_placing().click()
        print('Click button placing')

    #Methods

    def delete_and_add(self):

        self.click_select_delete_product_2()
        time.sleep(1)
        self.click_add_product_1()
        time.sleep(1)

    def placing_order(self):

        self.click_button_placing()
        time.sleep(1)
        self.assert_url('https://www.chipdip.ru/account/logon?ReturnUrl=%2forder%2fform%3ffrom%3dcart&from=cart')
        time.sleep(1)










