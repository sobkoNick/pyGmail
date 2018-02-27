from elements.baseElement import WebEl


class Button(WebEl):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)

    def click(self):
        self.element.click()