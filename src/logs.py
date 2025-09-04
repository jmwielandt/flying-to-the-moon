import logging


def config_logger(level: int):
    logging.basicConfig(level=level, format="%(asctime)s - %(levelname)s - %(message)s")
