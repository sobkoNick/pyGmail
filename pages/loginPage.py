from contants.constants import Constants
from elements.button import Button
from elements.input import Input
from locators.loginLocators import LoginLocators
from pages.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def openLoginPage(self):
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
