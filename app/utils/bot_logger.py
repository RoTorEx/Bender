import datetime
import logging
import os


def create_logger(file_name):
    """Init custom logger."""
    try:
        os.mkdir("data/logs")

    except FileExistsError:
        pass

    logger = logging.getLogger(file_name)
    key = datetime.datetime.strftime(datetime.datetime.now(), "%y-%m-%d_%H-%M")

    logging.basicConfig(
        level=logging.DEBUG,
        filename=f"data/logs/{key}_bot.log",
        filemode="a",
        datefmt="%d-%m-%y %H:%M:%S",
        format="[%(asctime)s] %(levelname)s (%(name)s) - %(message)s",
    )

    return logger
