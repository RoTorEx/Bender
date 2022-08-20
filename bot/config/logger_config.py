import datetime
import logging
from  logging.handlers import TimedRotatingFileHandler
import os


def create_logger(init_file_name):
    """Init custom logger."""
    if not os.path.exists("./data"):
        os.mkdir("./data")

    if not os.path.exists("./data/logs"):
        os.mkdir("./data/logs")

    logger = logging.getLogger(init_file_name)

    logging.basicConfig(
        level=logging.DEBUG,
        filename="data/logs/bot.log",
        filemode="a",
        datefmt="%d %m %y %H:%M:%S",
        format="[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
    )

    return logger
