
import sys
import os 


import QUANTAXIS as QA
from QUANTAXIS.QAAnalysis.QAAnalysis_finance import QAAnalysis_finance
from QUANTAXIS.QASetting.QALocalize import analysis_path
from factorBase import FactorBase
from factorClickhouse import FactorCKClient

from qaenv import (clickhouse_ip, clickhouse_password, clickhouse_port,
                   clickhouse_user)


from ind.Alpha101 import *

from tools import Sample_Tools as smpl
from tools import QAAdapter as qaadapter
# from tools import QAAdapter as qaadapter
# from tools import QA_adapter_get_code_from_block


class alpha101_1(FactorBase):

    def finit(self):

      self.clientr = FactorCKClient(clickhouse_ip, clickhouse_port, user=clickhouse_user, password=clickhouse_password)
      self.factor_name = 'alpha101_1'

    def calc(self, code_list, start_date, end_date) -> pd.DataFrame:
        """

        the example is just a day datasource, u can use the min data to generate a day-frequence factor

        the factor should be in day frequence 
        """
        data = QA.QA_fetch_stock_day_adv(code_list, start_date, end_date)

        cur_ret = smpl.get_current_return(data,'close')
        prices = data.data['close']

        factor = pd.DataFrame(alpha1(prices, cur_ret))
        factor = factor.replace([-np.inf, np.inf], 0).fillna(value=0)
        factor.columns = ['factor']

        return factor.reset_index().dropna()
