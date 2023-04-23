from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure

from base.base_class import Base
class Cart_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #loacators

    checkout_button="//button[@id='checkout']"



    #Getters

    def get_checkout_button(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))







    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")





        #Methods


    def product_confirmation(self):
        with allure.step("Product confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")





