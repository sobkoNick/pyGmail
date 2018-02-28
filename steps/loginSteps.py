from pages.loginPage import LoginPage


class LoginSteps:

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        self.logger = None

    def set_logger(self, logger):
        self.logger = logger

    def loginAndVerify(self, username, password):
        loginPage = LoginPage(driver=self.driver)
        self.logger.info("openning log in page")
        loginPage.openLoginPage()
        self.logger.info("inputting name")
        loginPage.inputEmail(username)
        self.logger.info("inputting password")
        loginPage.inputPassword(password)
        self.logger.info("click log in")
        loginPage.clickLogIn()
        self.logger.assertAndLog(loginPage.isUrlMatches("https://twitter.com/"), "url is not like twitter start url")