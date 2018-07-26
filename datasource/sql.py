from datasource import dataouttypes
import utils
import quandl
import config
import json
import sqlite3

class SqllDataSource:
    def __init__(self, columns=None):
        conn = sqlite3.connect(config.DB_FILE_PATH)
        self.cursor = conn.cursor()

    def __del__(self):
        if self.cursor:
            try:
                self.cursor.connection.close()
                self.cursor.close()
            except:
                pass

    def get_data(self, stock_code=None, start_date=None, end_date=None):

        self.cursor.execute("select * from stock where stock_code_nse=?", (stock_code,))

        res = self.cursor.fetchall()

        if len(res) == 0:
            return None

    def set_output_cols(self):
        pass

