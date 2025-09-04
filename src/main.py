from src.api.server import app
from src.config import app_config
from src.db.connect import connect_db
from src.logs import config_logger


def main():
    print("Hello from flying-to-the-moon!")
    config_logger(app_config.misc.log_level)
    connect_db()

    return app
