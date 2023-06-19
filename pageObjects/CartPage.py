from selenium import webdriver
from selenium.webdriver.common.by import By

class AddtoCart:
    add_item_by_Xpath= "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart_button_by_Xpath="//a[@class='shopping_cart_link']"
    removeFromCart_by_Xpath="//button[@id='remove-sauce-labs-backpack']"
    cart_items_by_Xpath="//div[@class='cart_item_label']"
    def __init__(self, driver):
        self.driver = driver

    def addtoitem(self):
        self.driver.find_element(By.XPATH,self.add_item_by_Xpath).click()

    def Clickcart(self):
        self.driver.find_element(By.XPATH,self.cart_button_by_Xpath).click()

    def removeCart(self):
        self.driver.find_element(By.XPATH,self.removeFromCart_by_Xpath).click()

    def cartItems(self):
        self.length=self.driver.find_elements(By.XPATH,self.cart_items_by_Xpath)
        return self.length
