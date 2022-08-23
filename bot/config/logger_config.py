import logging
import os


def create_logger(init_file_name):
    """Init custom logger."""
    if not os.path.exists("./logs"):
        os.mkdir("./logs")

    logger = logging.getLogger(init_file_name)

    logging.basicConfig(
        level=logging.DEBUG,
        filename="logs/bot.log",
        filemode="w",
        datefmt="%d %m %y %H:%M:%S",
        format="[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
    )

    return logger
