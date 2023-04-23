from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure

from base.base_class import Base
class Client_information_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #loacators

    first_name="//input[@id='first-name']"
    last_name="//input[@id='last-name']"
    postal_code="//input[@id='postal-code']"
    continue_button="//input[@id='continue']"



    #Getters

    def get_first_name(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))




    #Actions

    def input_first_name(self, user_name):
        self.get_first_name().send_keys(user_name)
        print("Input first name")


    def input_last_name(self, password):
        self.get_last_name().send_keys(password)
        print("Input last name")

    def input_postal_code(self, password):
        self.get_postal_code().send_keys(password)
        print("Input postal code")


    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")



        #Methods


    def input_information(self):
        with allure.step("Input information"):
            Logger.add_start_step(method="input_information")
            self.get_current_url()
            self.input_first_name("Graf")
            self.input_last_name("Farg")
            self.input_postal_code("450111")
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method="input_information")






