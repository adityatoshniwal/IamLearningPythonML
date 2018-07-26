import os
import sys

from stockcache import StockCacheManager
from setup import setup_app
setup_app()

root = os.path.dirname(os.path.realpath(__file__))
if sys.path[0] != root:
    sys.path.insert(0, root)

if __name__ == "__main__":

    print("Hello world !!")
    s = StockCacheManager()
    print(s.get_data("NSE/TCS", "2018-01-01", "2018-01-31", ["Open", "Close"]))
    print(s.get_data("NSE/TCS", "2018-01-01", "2018-01-20", ["Open", "Close"]))
