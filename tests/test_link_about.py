import time

import pages.login_page
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
import allure



@allure.description("Test link about")
def test_link_about(set_group):
    options=Options()
    options.add_experimental_option('excludeSwitches', ['enable-Logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

    login=pages.login_page.Login_page(driver)
    login.autorization()

    time.sleep(3)


    mp=pages.main_page.menu_buttons(driver)
    mp.select_buttons()










