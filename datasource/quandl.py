from datasource import dataouttypes
import utils
import quandl
import config

quandl.ApiConfig.api_key = config.QUANDL_API_KEY

class QuandlDataSource:
    def __init__(self, columns=None):
        self.columns = columns

    def check_required(self, required_inp, args_inp):
        pass

    def get_numpy_data(self, exchange, stock, from_date, to_date):
        """
        :param exchange:
        :param stock:
        :param from_date:
        :param to_date:
        :return: pandas dataframe
        """
        return quandl.get("{0}/{1}".format(exchange, stock), start_date=from_date, end_date=to_date,
                          returns="numpy")

    def get_dataframe_data(self, exchange, stock, from_date, to_date):
        """
        :param exchange:
        :param stock:
        :param from_date:
        :param to_date:
        :return: pandas dataframe
        """
        if len(self.columns) > 0:
            return quandl.get("{0}/{1}".format(exchange, stock), start_date=from_date, end_date=to_date)[self.columns]
        else:
            return quandl.get("{0}/{1}".format(exchange, stock), start_date=from_date, end_date=to_date)

    def get_json_data(self, exchange, stock, from_date, to_date):
        """
        :param exchange:
        :param stock:
        :param from_date:
        :param to_date:
        :return: pandas dataframe
        """
        return self.get_raw_data(exchange, stock, from_date, to_date).to_json();

    def get_data(self, exchange=None, stock=None, from_date=None,
                 to_date=None, out_type=dataouttypes.JSON):
        """
        :param exchange:
        :param stock:
        :param from_date:
        :param to_date:
        :return: pandas dataframe
        """
        requiredInp = ["exchange", "stock", "from_date", "to_date"]

        utils.check_required_args(locals(), requiredInp)

        if out_type == dataouttypes.JSON:
            return self.get_json_data(exchange, stock, from_date, to_date)
        else:
            return self.get_dataframe_data(exchange, stock, from_date, to_date)

    def set_output_cols(self):
        pass

