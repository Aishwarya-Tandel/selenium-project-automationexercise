import logging
import os

class Log_store:
    @staticmethod
    def get_log(name):
        folder = "logs"
        if not os.path.exists(folder):
            os.makedirs(folder)

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            path = os.path.join(folder,"test_logs.log")
            file_handler = logging.FileHandler(path)

            format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(lineno)d - %(funcName)s - %(message)s")
            file_handler.setFormatter(format)

            logger.addHandler(file_handler)

        return logger

