import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Product_page(Base):

    # Locators

    select_sort = '//span[@class="link link_dark filter__sort"]'
    select_filter_screen = '//*[@id="filter_x.2072"]/div/div[1]/div/div[2]'
    select_filter_screen_parameter_1 = '//*[@id="filter_x.2072"]/div/div[2]/div[2]/label[3]/span/span'
    select_filter_screen_parameter_2 = '//*[@id="filter_x.2072"]/div/div[2]/div[2]/label[4]/span/span'
    select_button_show = '//button[@id="formsubmitterbtn"]'
    select_filter_processor = '//*[@id="filter_x.7845"]/div/div[1]/div/div[2]'
    select_filter_processor_parameter_1 = '//*[@id="filter_x.7845"]/div/div[2]/div[2]/label[2]/span/span'
    select_filter_processor_parameter_2 = '//*[@id="filter_x.7845"]/div/div[2]/div[1]/label[10]/span/span'
    select_filter_processor_parameter_3 = '//*[@id="filter_x.7845"]/div/div[2]/div[3]/label[11]/span/span'
    select_product_1_cart = '//button[@data-id="qty_8025849556"]'
    select_product_1_name = '//a[@href="/product0/8025849556"]'
    select_product_1_price = '//span[@id="price_8025849556"]'
    select_product_2_cart = '//button[@data-id="qty_8025849471"]'
    select_product_2_name = '//a[@href="/product0/8025849471"]'
    select_product_2_price = '//span[@id="price_8025849471"]'
    select_cart_button = '//*[@id="headermain"]/div[2]/a[5]/div[1]'
    select_exit_advertising = '//div[@class="notification-reset-w"]'


    # Getters

    def get_select_sort(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_sort)))

    def get_select_filter_screen(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_filter_screen)))

    def get_select_filter_screen_parameter_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_filter_screen_parameter_1)))

    def get_select_filter_screen_parameter_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_filter_screen_parameter_2)))

    def get_select_button_show(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_button_show)))

    def get_select_filter_processor(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_filter_processor)))

    def get_select_filter_processor_parameter_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_filter_processor_parameter_1)))

    def get_select_filter_processor_parameter_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_filter_processor_parameter_2)))

    def get_select_filter_processor_parameter_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_filter_processor_parameter_3)))

    def get_select_product_1_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1_cart)))

    def get_select_product_1_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1_name)))

    def get_select_product_1_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1_price)))

    def get_select_product_2_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_2_cart)))

    def get_select_product_2_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_2_name)))

    def get_select_product_2_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_2_price)))

    def get_select_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_cart_button)))

    def get_select_exit_advertising(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_exit_advertising)))

    # Actions

    def click_select_sort(self):
        self.get_select_sort().click()
        print('Click sort')

    def click_select_filter_screen(self):
        self.get_select_filter_screen().click()
        print('Click select filter screen')

    def click_select_filter_screen_parameter_1(self):
        self.get_select_filter_screen_parameter_1().click()
        print('Click select filter screen parameter 1')

    def click_select_filter_screen_parameter_2(self):
        self.get_select_filter_screen_parameter_2().click()
        print('Click select filter screen parameter 2')

    def click_select_button_show(self):
        self.get_select_button_show().click()
        print('Click select button show')

    def click_select_filter_processor(self):
        self.get_select_filter_processor().click()
        print('Click select filter processor')

    def click_select_filter_processor_parameter_1(self):
        self.get_select_filter_processor_parameter_1().click()
        print('Click select filter processor parameter 1')

    def click_select_filter_processor_parameter_2(self):
        self.get_select_filter_processor_parameter_2().click()
        print('Click select filter processor parameter 2')

    def click_select_filter_processor_parameter_3(self):
        self.get_select_filter_processor_parameter_3().click()
        print('Click select filter processor parameter 3')

    def click_select_product_1_cart(self):
        self.get_select_product_1_cart().click()
        print('Click select product 1 cart')

    def save_select_product_1_name(self):
        product_1_name = self.get_select_product_1_name().text
        return product_1_name

    def save_select_product_1_price(self):
        product_1_price = self.get_select_product_1_price().text
        return product_1_price

    def click_select_product_2_cart(self):
        self.get_select_product_2_cart().click()
        print('Click select product 2 cart')

    def save_select_product_2_name(self):
        product_2_name = self.get_select_product_2_name().text
        return product_2_name

    def save_select_product_2_price(self):
        product_2_price = self.get_select_product_2_price().text
        return product_2_price

    def summa_products(self):
        product_1_price = self.save_select_product_1_price()
        product_2_price = self.save_select_product_2_price()
        summa_products = int(product_1_price.replace(' ', '')) + int(product_2_price.replace(' ', ''))
        return summa_products

    def click_select_cart_button(self):
        self.get_select_cart_button().click()
        print('Click cart button')

    def click_select_exit_advertising(self):
        self.get_select_exit_advertising().click()
        print('Click select exit advertising')


    #Methods

    def select_products(self):
        self.get_current_url()
        time.sleep(1)
        self.click_select_exit_advertising()
        time.sleep(1)
        self.click_select_sort()
        time.sleep(1)
        self.click_select_filter_screen()
        time.sleep(1)
        self.click_select_filter_screen_parameter_1()
        time.sleep(1)
        self.click_select_filter_screen_parameter_2()
        time.sleep(1)
        self.click_select_button_show()
        time.sleep(1)
        self.click_select_filter_processor()
        time.sleep(1)
        self.click_select_filter_processor_parameter_1()
        time.sleep(1)
        self.click_select_filter_processor_parameter_2()
        time.sleep(1)
        self.click_select_filter_processor_parameter_3()
        time.sleep(1)
        self.click_select_button_show()
        time.sleep(1)
        self.click_select_product_1_cart()
        time.sleep(1)
        print(f'Название первого продукта: {self.save_select_product_1_name()}')
        time.sleep(1)
        print(f'Цена первого продукта: {self.save_select_product_1_price()} рублей')
        time.sleep(1)
        self.click_select_product_2_cart()
        time.sleep(1)
        print(f'Название второго продукта: {self.save_select_product_2_name()}')
        time.sleep(1)
        print(f'Цена второго продукта: {self.save_select_product_2_price()} рублей')
        time.sleep(1)
        print(f'Цена продуктов в корзине: {self.summa_products()} рублей')
        self.click_select_cart_button()
        self.assert_url('https://www.chipdip.ru/cart')



