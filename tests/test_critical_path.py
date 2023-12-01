import time
import pytest
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.person_information_page import Person_information_page
from pages.product_page import Product_page


@pytest.mark.run(order=1)
def test_buy_product_1(set_up):
    driver = webdriver.Chrome()
    print('Start test 1')

    mp = Main_page(driver)
    mp.select_category_products()

    pp = Product_page(driver)
    pp.select_products()

    cp = Cart_page(driver)
    assert pp.save_select_product_1_name() == cp.save_select_product_1_name_cart()
    assert pp.save_select_product_2_name() == cp.save_select_product_2_name_cart()
    assert pp.summa_products() == cp.save_all_price_in_cart()
    print('Название и цены в корзине соответствуют изначальным')
    cp.delete_and_add()
    assert int(pp.save_select_product_1_price().replace(' ', '')) * 2 == cp.save_all_price_in_cart()
    print('После изменения в корзине цена верная')
    cp.placing_order()

    pipag = Person_information_page(driver)
    pipag.print_person_information()

    print('Finish test 1')
    time.sleep(1)
    driver.quit()
