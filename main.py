import os
import sys

from datasource import dataouttypes
from datasource.quandl import QuandlDataSource

root = os.path.dirname(os.path.realpath(__file__))
if sys.path[0] != root:
    sys.path.insert(0, root)

if __name__ == "__main__":
    print("Hello world !!")
    q = QuandlDataSource(columns=['Open', 'Close'])
    print(q.get_data("NSE", "TCS", "2018-01-01", "2018-01-31", dataouttypes.PANDAS_DATAFRAME))
