import os
import sys

from stockcache import StockCacheManager

from datasource import dataouttypes
from datasource.quandl import DataSource

root = os.path.dirname(os.path.realpath(__file__))
if sys.path[0] != root:
    sys.path.insert(0, root)

if __name__ == "__main__":
    print("Hello world !!")
    # q = DataSource(columns=['Open', 'Close'])
    # print(q.get_data("NSE", "TCS", "2018-01-01", "2018-01-31", dataouttypes.PANDAS_DATAFRAME).dtypes)
    s = StockCacheManager()
    print(s.get_stock_data("NSE/TCS", "2018-01-01", "2018-01-31"))
    print(s.get_stock_data("NSE/TCS", "2018-01-01", "2018-01-20"))
