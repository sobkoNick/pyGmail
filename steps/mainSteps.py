from time import sleep

from pages.mainPage import MainPage


class MainSteps():
    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        self.logger = None
        self.mainPage = MainPage(driver=self.driver)

    def set_logger(self, logger):
        self.logger = logger

    def writeTweet(self, tweet):
        mainPage = self.mainPage
        mainPage.writeTweet(tweet)
        mainPage.sendTweet()
        mainPage.clickOnGlobalPageBtn()
        sleep(3)
        self.veriryTweetText(1, tweet)

    def veriryTweetText(self, index, expectedText):
        mainPage = self.mainPage
        actualText = mainPage.getTweetText(index)
        self.logger.assertAndLog(expectedText in actualText, "Actual %s text does not have expected %s text" % (actualText, expectedText))
