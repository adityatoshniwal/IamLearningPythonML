from datasource import dataouttypes
import quandl
from datasource.quandl import QuandlDataSource
from datasource.sql import SqllDataSource


class DataSource:
    def __init__(self):
        self.quandlDB = QuandlDataSource()
        self.sqlDB = SqllDataSource()

    def get_data(self, stock_code=None, start_date=None,
                 end_date=None, columns=None, out_type=dataouttypes.PANDAS_DATAFRAME):
        """
        :param exchange:
        :param stock:
        :param start_date:
        :param end_date:
        :return: pandas dataframe
        """

        self.stockdata = self.sqlDB.get_data()
        if not self.stockdata:
            if columns is not None and len(columns) > 0:
                self.stockdata = self.quandlDB.get_data(stock_code, start_date=start_date, end_date=end_date, columns=columns)
            else:
                self.stockdata = self.quandlDB.get_data(stock_code, start_date=start_date, end_date=end_date)

        return self.stockdata

    def set_output_cols(self):
        pass

