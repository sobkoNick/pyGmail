from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WebEl(object):
    """Base page class that is initialized on every page object class."""

    element = None  # type:WebElement

    def __init__(self, driver, locator):
        self.driver = driver # type:WebDriver
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locator)))
        self.element = driver.find_element_by_xpath(locator)

    def getValue(self):
        return self.element.get_attribute("value")

    def getAttribute(self, attrName):
        return self.element.get_attribute(attrName)
