import logging
import pathlib
import os

import conftest


class Nextlogger:
    def set_up_logger(self, name):

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        pathlib.Path(conftest.ROOT_DIR + "\\logs\\").mkdir(exist_ok=True)

        logPath = conftest.ROOT_DIR + "\\logs\\" + name + ".log"

        if os.path.isfile(logPath):
            os.remove(logPath)

        fileHandler = logging.FileHandler(logPath)
        fileHandler.setLevel(logging.DEBUG)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        consoleHandler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(fileHandler)

        logger.addHandler(consoleHandler)

        self.logger = logger

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warn(self, message):
        self.logger.warn(message)

    def exception(self, meassage):
        self.logger.exception(meassage)

    def assertAndLog(self, verification, msg):
        if not verification:
            self.logger.error(msg)
            try:
                assert verification, msg
            except AssertionError:
                raise