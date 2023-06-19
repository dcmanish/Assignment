import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.CartPage import AddtoCart
from pageObjects.CheckoutPage import Checkout
from Utilities.readProperties import ReadConfig



class Test_003_Checkout:
    baseURL = ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    firstname="abc"
    lastname="xyz"
    postalcode="12345"

    def test_checkout(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(2)

        # item added to the cart
        self.ac=AddtoCart(self.driver)
        self.ac.addtoitem()
        self.ac.Clickcart()
        time.sleep(2)

        # Proceed to checkout
        self.ck = Checkout(self.driver)
        self.ck.checkoutClick()

        # Enter checkout information
        self.ck.firstname(self.firstname)
        self.ck.Lastname(self.lastname)
        self.ck.postalcode(self.postalcode)
        time.sleep(2)

        self.ck.Click_Continue()
        time.sleep(2)
        self.information=self.driver.page_source

        # Verify the order summary
        assert "Payment Information" in self.information
        assert "Shipping Information" in self.information
        assert "Item total: $" in self.information

        self.ck.Click_Finish()

        # Verify the order confirmation
        self.sucess = self.driver.page_source
        assert "Thank you for your order!" in self.sucess
