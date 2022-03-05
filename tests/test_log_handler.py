import logging

import pytest

from src.Log_handler import LoggHandler


def test_init(mocker):
    mocker.patch("logging.Logger.setLevel")

    LoggHandler("Testlevel_DEBUG")
    logging.Logger.setLevel.assert_called_with(logging.DEBUG)

    LoggHandler("Teslevel_INFO", logging.INFO)
    logging.Logger.setLevel.assert_called_with(logging.INFO)

    mocker.patch("logging.getLogger")
    LoggHandler("TestGet")
    logging.getLogger.assert_called_with("TestGet")


def test_start_logger(mocker):
    mocker.patch("logging.Logger.addHandler")

    logger = LoggHandler("TestLog")
    logger.start_logger()
    logging.Logger.addHandler.assert_called()