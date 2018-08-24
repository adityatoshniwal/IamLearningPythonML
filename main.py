import os
import sys

from stockcache import StockCacheManager
from setup import setup_app
setup_app()

import matplotlib.pyplot as mplot
root = os.path.dirname(os.path.realpath(__file__))
if sys.path[0] != root:
    sys.path.insert(0, root)

if __name__ == "__main__":

    print("Hello world !!")
    s = StockCacheManager()

    stockData = s.get_data("NIFTY", "2018-04-01", "2018-04-30", ["Open", "Close"])
    #print(s.get_data("NSE/TCS", "2018-01-01", "2018-01-31", ["Open", "Close"]))

    # SMA
    days = 5
    calcData = stockData.loc[:,["CLOSE"]]
    calcData['SMA'] = calcData.loc[:,["CLOSE"]].rolling(window=days).mean()
    calcData['STD'] = calcData.loc[:,["CLOSE"]].rolling(window=days).std()
    calcData['UBAND'] = calcData['SMA'] + calcData['STD'] * 2
    calcData['LBAND'] = calcData['SMA'] - calcData['STD'] * 2

    calcData.plot()
    mplot.ylabel('Price (Rs)')
    mplot.xlabel('Price (Rs)')
    mplot.show();
