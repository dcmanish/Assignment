import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    def test_homePageTitle(self, setup):

        # Set up the driver
        self.driver=setup     # Assuming you have ChromeDriver installed and in your PATH

        # Open the website
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots"+"test_homePageTitle.png")
            assert False

    def test_login(self,setup):

        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        # Enter username and password
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        # Verify that the user is logged in
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Swag Labs":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_login.png")
            assert False





