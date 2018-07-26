from datasource import dataouttypes
import utils
import quandl
import config
import json

quandl.ApiConfig.api_key = config.QUANDL_API_KEY


class QuandlDataSource:
    def __init__(self):
        pass

    def get_numpy_data(self, stock_code, start_date, end_date):
        """
        :param exchange:
        :param stock:
        :param start_date:
        :param end_date:
        :return: pandas dataframe
        """
        return quandl.get(stock_code, start_date=start_date, end_date=end_date,
                          returns="numpy")

    def get_dataframe_data(self, stock_code, start_date, end_date):
        """
        :param exchange:
        :param stock:
        :param start_date:
        :param end_date:
        :return: pandas dataframe
        """
        return quandl.get(stock_code, start_date=start_date, end_date=end_date)

    def get_json_data(self, stock_code, start_date, end_date):
        """
        :param exchange:
        :param stock:
        :param start_date:
        :param end_date:
        :return: pandas dataframe
        """
        return json.dumps(self.get_dataframe_data(stock_code, start_date, end_date).to_dict())

    def get_data(self, stock_code=None, start_date=None,
                 end_date=None, out_type=dataouttypes.PANDAS_DATAFRAME):

        if out_type == dataouttypes.JSON:
            return self.get_json_data(stock_code, start_date, end_date)
        elif out_type == dataouttypes.NUMPY:
            return self.get_numpy_data(stock_code, start_date, end_date)
        else:
            return self.get_dataframe_data(stock_code, start_date, end_date)

    def set_output_cols(self):
        pass

