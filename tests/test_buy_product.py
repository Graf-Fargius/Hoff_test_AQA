import time

import pages.login_page
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.payment_page import Payment_page
from pages.finish_button import Finish_page
from selenium.webdriver.chrome.options import Options



# @pytest.mark.run(order=3)
@allure.description("Test buy product 1")
def test_buy_product_1(set_group):
    options=Options()
    options.add_experimental_option('excludeSwitches', ['enable-Logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

    print("Start Test 1")


    login=pages.login_page.Login_page(driver)
    login.autorization()


    mp=pages.main_page.Main_page(driver)
    mp.select_products_1()

    time.sleep(3)

    cp=pages.cart_page.Cart_page(driver)
    cp.product_confirmation()

    cip= Client_information_page(driver)
    cip.input_information()

    pay=Payment_page(driver)
    pay.payment()
    f=Finish_page(driver)
    f.finish()

    print("Finish Test 1")
    # time.sleep(10)


# @pytest.mark.run(order=1)
# def test_buy_product_2(set_group):
#     options=Options()
#     options.add_experimental_option('excludeSwitches', ['enable-Logging'])
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
#
#     print("Start Test 2")
#
#
#     login=pages.login_page.Login_page(driver)
#     login.autorization()
#
#
#     mp=pages.main_page.Main_page(driver)
#     mp.select_products_2()
#
#     time.sleep(3)
#
#     cp=pages.cart_page.Cart_page(driver)
#     cp.product_confirmation()
#
#     print("Finish Test 2")
# #     time.sleep(10)
# #
# #
# #
# # @pytest.mark.run(order=2)
# def test_buy_product_3():
#     options=Options()
#     options.add_experimental_option('excludeSwitches', ['enable-Logging'])
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
#
#     print("Start Test 3")
#
#
#     login=pages.login_page.Login_page(driver)
#     login.autorization()
#
#
#     mp=pages.main_page.Main_page(driver)
#     mp.select_products_3()
#
#     time.sleep(3)
#
#     cp=pages.cart_page.Cart_page(driver)
#     cp.product_confirmation()
#
#     print("Finish Test 3")
# #     time.sleep(10)











