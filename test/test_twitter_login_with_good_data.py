def test_login_001(app, excel_credentials):
    app.nLogger.set_up_logger(__name__)
    logger = app.nLogger
    logger.info(__name__  + " start")

    user = excel_credentials
    loginStep = app.loginStep
    loginStep.set_logger(logger)

    loginStep.loginAndVerify(username=user.username, password=user.password)

    logger.info(__name__ + " finish with success")

