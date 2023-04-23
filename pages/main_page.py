from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure

from base.base_class import Base
class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #loacators

    select_product_1="//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart="//div[@class='shopping_cart_container']"


    #Getters

    def get_select_product_1(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    #Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select_product_1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select_product_2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click select_product_3")

    def click_cart(self):
        self.get_cart().click()
        print("Click click_cart")


        #Methods


    def select_products_1(self):
        with allure.step("Select products 1"):
            Logger.add_start_step(method="select_products_1")
            self.get_current_url()
            self.click_select_product_1()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_products_1")

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()



class menu_buttons(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    # loacators

    burger_menu_button = "//div[@class='bm-burger-button']"
    about_button = "//a[@id='about_sidebar_link']"

    # Getters

    def get_burger_menu_button(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu_button)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_button)))

        # Actions

    def click_burger_menu_button(self):
        self.get_burger_menu_button().click()
        print("Click burger menu button")

    def click_about_button(self):
        self.get_about_button().click()
        print("Click about button")

        # Methods

    def select_buttons(self):
        with allure.step("Select buttons"):
            self.get_current_url()
            self.click_burger_menu_button()
            self.click_about_button()
            self.assert_url("https://saucelabs.com/")
