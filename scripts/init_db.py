import logging

from rethinkdb import r

from src.config import app_config
from src.db.connect import connect_db
from src.logs import config_logger

config_logger(app_config.misc.log_level)
con = connect_db(app_config.db.host, app_config.db.port, app_config.db.name)

r.db_create(app_config.db.name)

if "flights" in r.table_list().run(con):
    logging.warning("table 'flights' already exists")
else:
    r.table_create("flights").run(con)


con.close()
