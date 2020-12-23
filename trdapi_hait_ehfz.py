#!/usr/bin/python38
# coding: utf-8
# Author: Maxincer
# CreateDateTime: 20201217T160000

from concurrent.futures import ThreadPoolExecutor
from ctypes import *
from datetime import datetime
from time import sleep

from pymongo import MongoClient

from api_hait_ehfz.jgtrade_api import *
from api_hait_ehfz.jgtrade_api_func_def import *
from api_hait_ehfz.trade_stock_call_dll import *
from api_hait_ehfz.jgtrade_api_data_def import *


class DldTrdDataFromEHFZApi:
    def __init__(self):
        client_mongodb = MongoClient('mongodb://192.168.2.162:27017/')
        db_basicinfo = client_mongodb['basicinfo']
        self.col_acctinfo = db_basicinfo['acctinfo']
        self.dt_today = datetime.today()
        self.str_today = self.dt_today.strftime('%Y%m%d')
        self.list_dicts_acctinfo = list(
            self.col_acctinfo.find({'DataDate': self.str_today, 'DataSourceType': 'hait_ehfz', 'DataDownloadMark': 1})
        )
        self.dirpath_output = 'D:/data/trddata/investment_manager_products/hait_ehfz'
        self.g_serviceid = ''
        self._jgtradeapi_notice_cb_ = OnTradeLinkCallBack(OnNoticeData)
        self._jgtradeapi_data_cb_ = OnTradeDataCallBack(OnRecvData)
        API_Start()

    def dlddata_by_acctidbymxz(self, acctidbybroker, accttype):
        # 账户类型调整: 现金账户 vs 保证金账户
        if accttype in ['c']:
            self.g_serviceid = API_CreateService(TRADETYPE.TD_STOCK.value)
            register_Linkcallback(self.g_serviceid, self._jgtradeapi_notice_cb_)
            register_Datacallback(self.g_serviceid, self._jgtradeapi_data_cb_)
            API_Connect(self.g_serviceid, c_char_p(b"124.74.252.82"), 8980, False)  # 此处传参： 交易服务器参数
            sleep(0.1)
            log_in(acctidbybroker, '123321', self.g_serviceid)
            sleep(1)
            query_cacct_fund(self.g_serviceid)
            sleep(0.2)
            query_cacct_holding(self.g_serviceid)
            sleep(0.2)
            query_cacct_trade(self.g_serviceid)
            sleep(0.2)
            API_DisConnect(self.g_serviceid)

        elif accttype in ['m']:
            self.g_serviceid = API_CreateService(TRADETYPE.TD_CREDIT.value)
            register_Linkcallback(self.g_serviceid, self._jgtradeapi_notice_cb_)
            register_Datacallback(self.g_serviceid, self._jgtradeapi_data_cb_)
            API_Connect(self.g_serviceid, c_char_p(b"124.74.252.82"), 8980, False)  # 此处传参： 交易服务器参数
            sleep(0.1)
            log_in(acctidbybroker, '123321', self.g_serviceid)
            sleep(1)

            query_macct_fund(self.g_serviceid)
            sleep(0.2)
            query_macct_holding(self.g_serviceid)
            sleep(0.2)
            query_macct_trade(self.g_serviceid)
            sleep(0.2)
            query_short_sell(self.g_serviceid)
            sleep(0.2)
            API_DisConnect(self.g_serviceid)

        elif accttype in ['f', 'o']:
            pass

        else:
            raise ValueError('Unknown account type, please check.')

    def run(self):
        while True:
            for dict_acctinfo in self.list_dicts_acctinfo:
                acctidbybroker = dict_acctinfo['AcctIDByBroker']
                accttype = dict_acctinfo['AcctType']
                self.dlddata_by_acctidbymxz(acctidbybroker, accttype)
                print(f'{acctidbybroker} dld finished.')
            sleep(10)


if __name__ == '__main__':
    task = DldTrdDataFromEHFZApi()
    task.run()
















