from selenium.webdriver.remote.webdriver import WebDriver

from contants.constants import Constants
from elements.button import Button
from elements.input import Input
from locators.loginLocators import LoginLocators
from pages.basePage import BasePage


class Login(BasePage):
    def __init__(self, app, driver):
        super().__init__(driver)
        self.app = app

    def openLoginPage(self):
        self.driver = self.app.driver  # type:WebDriver
        self.driver.get(Constants.LOGIN_URL)

    def inputEmail(self, emailOrName):
        email = Input(driver=self.driver, locator=LoginLocators.EMAIL_BOX)
        email.clear()
        email.setText(emailOrName)

    def inputPassword(self, password):
        passwordField = Input(driver=self.driver, locator=LoginLocators.PASSWORD_BOX)
        passwordField.clear()
        passwordField.setText(password)

    def clickLogIn(self):
        logInBtn = Button(driver=self.driver, locator=LoginLocators.SIGN_UP_BTN)
        logInBtn.click()

