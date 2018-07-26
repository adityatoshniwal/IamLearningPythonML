import utils
from datasource import DataSource


class StockCacheManager:
    """
    This class will create a cache. If a request for a stock is made, this will
    check in the cache first and if data is available for given date range then
    will return from cache else will fetch from datasource
    """
    def __init__(self):
        self.stock_cache = {}
        self.datasource = DataSource()

        # We will use this to pass data within the class as data can be huge
        # and we do not want data passing overhead
        self.stockdata = None

    def add_stock_to_cache(self, stock_code, start_date, end_date):
        self.stock_cache[stock_code] = {
            "start_date": utils.string_end_date(start_date),
            "end_date": utils.string_end_date(end_date),
            "data": self.stockdata
        }

    def get_data(self, stock_code, start_date, end_date, columns):
        if stock_code in self.stock_cache:
            print('From Cache')
            return self.stock_cache[stock_code]["data"][utils.string_end_date(start_date):utils.string_end_date(end_date)]
        else:
            print('From Datasource')
            self.stockdata = self.datasource.get_data(stock_code, start_date, end_date)
            self.add_stock_to_cache(stock_code, start_date, end_date)

        return self.stockdata
