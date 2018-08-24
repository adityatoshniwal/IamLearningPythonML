import pandas as pd
import os
import config

class FileSource:
    def __init__(self, colNames=[], dateTimeCols=[], useColsNo=()):
        self.stockdata = None
        self.colNames = colNames
        self.dateTimeCols = dateTimeCols
        self.useColsNo = useColsNo


    def get_data(self, path):
        self.stockdata = pd.read_csv(path, usecols=self.useColsNo, parse_dates=[self.dateTimeCols], index_col=0,
                                     names=self.colNames)
        return self.stockdata