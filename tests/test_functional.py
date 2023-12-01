import time
import pytest
from selenium import webdriver
from pages.calculator_page import Calculator_page
from pages.feedback_page import Feedback_page
from pages.main_page import Main_page



@pytest.mark.run(order=3)
def test_feedback_form(set_group):
    driver = webdriver.Chrome()
    print('Start test 1')

    mp = Main_page(driver)
    mp.feedback_check()

    fp = Feedback_page(driver)
    fp.print_information()

    print('Finish test 1')
    time.sleep(1)
    driver.quit()


@pytest.mark.run(order=2)
def test_calculators(set_group):
    driver = webdriver.Chrome()
    print('Start test 2')

    mp = Main_page(driver)
    mp.calculator_check()

    calcp = Calculator_page(driver)
    calcp.check_capacitor_calculator()

    print('Finish test 2')
    time.sleep(1)
    driver.quit()
