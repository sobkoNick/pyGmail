from selenium import webdriver

import conftest
from pages.loginPage import LoginPage
from steps.loginSteps import LoginSteps
from steps.mainSteps import MainSteps
from utils import NextLogger


class Application:
    def __init__(self, browser):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome(conftest.ROOT_DIR + "\\chromedriver.exe")
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

        self.nLogger = NextLogger.Nextlogger()

        self.loginStep = LoginSteps(driver=self.driver)  # reference to SessionHelper which has login() method
        self.nLogger.set_up_logger(__name__)
        self.loginStep.set_logger(self.nLogger)

        self.mainStep = MainSteps(driver=self.driver)

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
