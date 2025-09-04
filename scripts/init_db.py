import logging

from rethinkdb import r

from src.config import app_config
from src.db.connect import connect_db
from src.logs import config_logger

config_logger(app_config.misc.log_level)
con = connect_db()

r.db_create(app_config.db.name)

tables_list: list[str] = r.table_list().run(con)

if "flights" in tables_list:
    logging.warning("table 'flights' already exist")
else:
    r.table_create("flights").run(con)
    logging.info("table flights created")

con.close()
