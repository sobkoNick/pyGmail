from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.basePage import BasePage
from pages.locators.mainLocators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def writeTweet(self, meassage):
        writeInput = Input(driver=self.driver, locator=MainPageLocators.WHAT_IS_GOING_ON_FIELD)
        writeInput.clear()
        writeInput.setText(meassage)

    def sendTweet(self):
        sendBtn = Button(driver=self.driver, locator=MainPageLocators.SEND_TWIT)
        sendBtn.click()

    def getTweetText(self, tweetIndex):
        tweetLocator = MainPageLocators.STREAM_TWEETS + "[%s]" % tweetIndex + MainPageLocators.TEXT_IN_TWEET
        tweetText = Text(self.driver, tweetLocator)
        return tweetText.getText()

    def clickOnGlobalPageBtn(self):
        gpb = Button(self.driver, MainPageLocators.GLOBAL_HOME_BTN)
        gpb.click()