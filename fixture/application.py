from selenium import webdriver

import conftest
from pages.loginPage import Login


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
        self.loginPage = Login(self, driver=self.driver)  # reference to SessionHelper which has login() method

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
