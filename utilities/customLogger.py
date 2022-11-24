import logging

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(
        #                     filename="C:\\Users\\User\\PycharmProjects\\nopcommerceApp\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s',
        #                     datefmt='%Y-%m-%d, %H:%M:%S.%f'
        #                     )

        # logging.basicConfig(filename="C:\\Users\\User\\PycharmProjects\\nopcommerceApp\\Logs\\automation1.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s')

        logger = logging.getLogger(__name__)
        # FileHandler class to set the location of log file
        fileHandler = logging.FileHandler('C:\\Users\\User\\PycharmProjects\\nopcommerceApp\\Logs\\automation2.log')
        logger.addHandler(fileHandler)

        # Formatter class to set the format of log file
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        # setting logging level to INFO
        logger.setLevel(logging.INFO)
        return logger
