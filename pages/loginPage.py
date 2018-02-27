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

    def inputLoginAndSubmit(self, username):
        driver = self.app.driver  # type:WebDriver
        driver.get(Constants.LOGIN_URL)

        email = Input(driver=driver, locator=LoginLocators.EMAIL_BOX)
        email.setText(username)

        nextBtn = Button(driver=driver, locator=LoginLocators.NEXT_BTN)
        nextBtn.click()

        # add assertion

    def inputPasswordAndSubmit(self, password):
        driver = self.app.driver  # type:WebDriver

        passwordField = Input(driver=driver, locator=LoginLocators.PASSWORD_BOX)
        passwordField.setText(password)

        nextBtn = Button(driver=driver, locator=LoginLocators.PASSWORD_NEXT_BTN)
        nextBtn.click()

