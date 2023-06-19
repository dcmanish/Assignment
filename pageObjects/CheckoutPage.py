from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class Checkout:

    # Enter checkout information
    first_name_by_Id = "first-name"
    last_name_by_Id="last-name"
    postal_code_by_Id = "postal-code"
    continue_button_by_Id = "continue"
    checkout_name = "checkout"
    finish_button_by_Id = "finish"
    scucess_msg_by_Xpath = "//h2[normalize-space()='Thank you for your order!']"

    def __init__(self, driver):
        self.driver = driver

    def firstname(self, firstname):
        self.driver.find_element(By.ID,self.first_name_by_Id).clear()
        self.driver.find_element(By.ID, self.first_name_by_Id).send_keys(firstname)

    def Lastname(self, lastname):
        self.driver.find_element(By.ID, self.last_name_by_Id).clear()
        self.driver.find_element(By.ID, self.last_name_by_Id).send_keys(lastname)

    def postalcode(self, code):
        self.driver.find_element(By.ID, self.postal_code_by_Id).clear()
        self.driver.find_element(By.ID, self.postal_code_by_Id).send_keys(code)

    def checkoutClick(self):
        self.driver.find_element(By.NAME, self.checkout_name).click()

    def Click_Continue(self):
        self.driver.find_element(By.ID, self.continue_button_by_Id).click()

    def Click_Finish(self):
        self.driver.find_element(By.ID, self.finish_button_by_Id).click()

