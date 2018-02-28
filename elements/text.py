from elements.baseElement import WebEl


class Text(WebEl):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)