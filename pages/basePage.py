class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver # type:WebDriver

    def is_title_contains(self, title):
        return title in self.driver.title

    def getCurrentUrl(self):
        return self.driver.current_url

    def isUrlMatches(self, url):
        return url == self.driver.current_url
