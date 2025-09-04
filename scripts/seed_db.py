import json

from rethinkdb import r

from src.config import app_config
from src.db.connect import connect_db
from src.logs import config_logger

config_logger(app_config.misc.log_level)
con = connect_db()


with open("scripts/passengers_20.json", "r", encoding="utf-8") as f:
    passengers = json.load(f)

r.table("passengers").insert(passengers).run(con)
