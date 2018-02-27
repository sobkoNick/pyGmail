def test_login_001(app, excel_credentials):
    user = excel_credentials
    app.loginPage.inputLoginAndSubmit(username=user.username)
    app.loginPage.inputPasswordAndSubmit(password=user.password)
