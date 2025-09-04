from rethinkdb import r


def connect_db(host: str, port: int, db: str):
    return r.connect(host, port, db=db)
