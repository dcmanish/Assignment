from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    username_by_Id = "user-name"
    password_by_Id= "password"
    login_button_by_Id = "login-button"
    menu_button_by_Xpath="//button[@id='react-burger-menu-btn']"
    logout_button_by_Xpath="//button[@id='react-burger-menu-btn']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.username_by_Id).clear()
        self.driver.find_element(By.ID,self.username_by_Id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.password_by_Id).clear()
        self.driver.find_element(By.ID,self.password_by_Id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.ID,self.login_button_by_Id).click()


    def clickMenu(self):
        self.driver.find_element(By.XPATH,self.clickMenu()).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.clickLogout()).click()
