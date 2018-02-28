def test_login_001(app, excel_credentials):
    user = excel_credentials
    app.loginPage.openLoginPage()
    app.loginPage.inputEmail(emailOrName=user.username)
    app.loginPage.inputPassword(password=user.password)
    app.loginPage.clickLogIn()

