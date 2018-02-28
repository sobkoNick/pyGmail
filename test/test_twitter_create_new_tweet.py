import datetime


def test_create_new_tweet(app):
    app.nLogger.set_up_logger(__name__)
    logger = app.nLogger
    logger.info(__name__ + " start")

    mainStep = app.mainStep
    mainStep.set_logger(logger)

    mainStep.writeTweet("Some simple pytest tweet" + str(datetime.datetime.now()))

    logger.info(__name__ + " finish with success")
