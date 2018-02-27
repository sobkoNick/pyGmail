from selenium.webdriver.common.by import By


class LoginLocators(object):
    EMAIL_BOX = '//*[@type="email"]'
    PASSWORD_BOX = '//*[@type="password"]'
    NEXT_BTN = '//*[@role="button" and @id="identifierNext"]'
    PASSWORD_NEXT_BTN = '//*[@role="button" and @id="passwordNext"]'
