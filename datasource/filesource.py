import pandas as pd
import os
import config

class FileSource:
    def __init__(self):
        self.stockdata = None

    def get_data(self, path):
        self.stockdata = pd.read_csv(path, usecols=range(1, 7), parse_dates=[[0, 1]], index_col=0,
                                     names=["DATE", "TIME", "OPEN", "HIGH", "LOW", "CLOSE"])
        return self.stockdata