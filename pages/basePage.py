class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self, title):
        return title in self.driver.title
