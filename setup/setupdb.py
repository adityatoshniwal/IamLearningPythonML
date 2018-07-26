import config
import sqlite3
import os
import config


def setup_db(hard=False):
    with open(os.path.join(config.APP_ROOT, "setup/base.sql")) as basesql:
        sql_script = basesql.read()

    if hard and os.path.exists(config.DB_FILE_PATH):
        os.remove(config.DB_FILE_PATH)

    if not os.path.exists(config.DB_FILE_PATH):
        conn = sqlite3.connect(config.DB_FILE_PATH)
        cur = conn.cursor()
        cur.executescript(sql_script)
