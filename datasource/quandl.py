from datasource import dataouttypes
import utils
import quandl
import config
import json

quandl.ApiConfig.api_key = config.QUANDL_API_KEY

class DataSource:
    def __init__(self, columns=None):
        self.columns = columns

    def check_required(self, required_inp, args_inp):
        pass

    def get_numpy_data(self, stock_code, from_date, to_date):
        """
        :param exchange:
        :param stock:
        :param from_date:
        :param to_date:
        :return: pandas dataframe
        """
        return quandl.get(stock_code, start_date=from_date, end_date=to_date,
                          returns="numpy")

    def get_dataframe_data(self, stock_code, from_date, to_date):
        """
        :param exchange:
        :param stock:
        :param from_date:
        :param to_date:
        :return: pandas dataframe
        """
        if len(self.columns) > 0:
            return quandl.get(stock_code, start_date=from_date, end_date=to_date)[self.columns]
        else:
            return quandl.get(stock_code, start_date=from_date, end_date=to_date)

    def get_json_data(self, stock_code, from_date, to_date):
        """
        :param exchange:
        :param stock:
        :param from_date:
        :param to_date:
        :return: pandas dataframe
        """
        return json.dumps(self.get_dataframe_data(stock_code, from_date, to_date).to_dict())

    def get_data(self, stock_code=None, from_date=None,
                 to_date=None, out_type=dataouttypes.JSON):

        if out_type == dataouttypes.JSON:
            return self.get_json_data(stock_code, from_date, to_date)
        elif out_type == dataouttypes.NUMPY:
            return self.get_numpy_data(stock_code, from_date, to_date)
        else:
            return self.get_dataframe_data(stock_code, from_date, to_date)

    def set_output_cols(self):
        pass

