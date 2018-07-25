import utils
from datasource import dataouttypes
from datasource.quandl import DataSource


class StockCacheManager:
    """
    This class will create a cache. If a request for a stock is made, this will
    check in the cache first and if data is available for given date range then
    will return from cache else will fetch from datasource
    """
    def __init__(self):
        self.stock_cache = {}
        self.datasource = DataSource(columns=['Open', 'Close'])

        # We will use this to pass data within the class as data can be huge
        # and we do not want data passing overhead
        self.stockdata = None

    def add_stock_to_cache(self, stock_code, from_date, to_date):
        self.stock_cache[stock_code] = {
            "from_date": utils.string_to_date(from_date),
            "to_date": utils.string_to_date(to_date),
            "data": self.stockdata
        }

    def get_stock_data(self, stock_code, from_date, to_date):
        if stock_code in self.stock_cache:
            print('From Cache')
            return self.stock_cache[stock_code]["data"][utils.string_to_date(from_date):utils.string_to_date(to_date)]
        else:
            print('From Quandl')
            self.stockdata = self.datasource.get_data(stock_code, from_date, to_date, dataouttypes.PANDAS_DATAFRAME)
            self.add_stock_to_cache(stock_code, from_date, to_date)

        return self.stockdata