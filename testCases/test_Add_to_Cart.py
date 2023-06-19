import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.CartPage import AddtoCart
from Utilities.readProperties import ReadConfig


class Test_002_AddtoCart:
    baseURL = ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()


    def test_AddtoCart(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.ac=AddtoCart(self.driver)

        # item added to the cart
        self.ac.addtoitem()
        time.sleep(2)
        self.ac.Clickcart()
        time.sleep(2)

        # Remove the item from the cart
        self.ac.removeCart()
        time.sleep(2)
        self.cartlen=len(self.ac.cartItems())
        self.driver.close()

        # Check if the cart is empty
        if self.cartlen == 0:
            assert True
        else:
            assert False









