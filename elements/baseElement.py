from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait


class WebEl(object): # type:WebElement
    """Base page class that is initialized on every page object class."""

    element = None  # type:WebElement

    def __init__(self, driver, locator):
        self.driver = driver # type:WebDriver
        self.locator = locator
        webWait = WebDriverWait(driver=driver, timeout=10)
        self.element = webWait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))

    def getValue(self):
        return self.element.get_attribute("value")

    def getAttribute(self, attrName):
        return self.element.get_attribute(attrName)

    def getText(self):
        return self.element.text
