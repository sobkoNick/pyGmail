from elements.baseElement import WebEl


class Input(WebEl):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)

    def setText(self, value):
        self.element.send_keys(value)

    def clear(self):
        self.element.clear()
