from selenium.webdriver.common.by import By


class LoginLocators(object):
    EMAIL_BOX = '(//*[contains(@class, "LoginForm-username")])[1]/input'
    PASSWORD_BOX = '(//*[contains(@class, "LoginForm-password")])[1]/input'
    SIGN_UP_BTN = '(//input[@type="submit"])[1]'
