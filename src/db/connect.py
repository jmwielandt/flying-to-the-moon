from rethinkdb import r

from src.config import app_config


def connect_db():
    return r.connect(app_config.db.host, app_config.db.port, db=app_config.db.name)
