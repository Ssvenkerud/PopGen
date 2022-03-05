import logging


class LoggHandler:
    def __init__(self, loggername, logger_level=logging.DEBUG):
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(logger_level)
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

    def __add_file_logger(self, logfile, file_level=logging.DEBUG):
        fh = logging.FileHandler(logfile)
        fh.setLevel(file_level)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

    def __add_console_logger(self, console_level=logging.ERROR):
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def start_logger(self, logfile="logs/log.log"):
        self.__add_file_logger(logfile)
        self.__add_console_logger()
        return self.logger
