#!/usr/bin/python38
# coding: utf-8
# Author: Maxincer
# CreateDateTime: 20201217T160000

from ctypes import *
from datetime import datetime

from pymongo import MongoClient

from api_hait_ehfz.jgtrade_api import *
from api_hait_ehfz.jgtrade_api_func_def import *
from api_hait_ehfz.trade_stock_call_dll import *
from api_hait_ehfz.jgtrade_api_data_def import *


class DldTrdDataFromEHFZApi:
    def __init__(self):
        self.host_apama = '139.196.103.39'
        self.port_apama = 22
        client_mongodb = MongoClient('mongodb://192.168.2.162:27017/')
        db_basicinfo = client_mongodb['basicinfo']
        self.col_acctinfo = db_basicinfo['acctinfo']
        self.dt_today = datetime.today()
        self.str_today = self.dt_today.strftime('%Y%m%d')
        self.list_dicts_acctinfo = list(
            self.col_acctinfo.find({'DataDate': self.str_today, 'DataSourceType': 'hait_ehfz', 'DataDownloadMark': 1})
        )
        self.dirpath_output = 'D:/data/trddata/investment_manager_products/hait_ehfz'
        self._jgtradeapi_notice_cb_ = OnTradeLinkCallBack(OnNoticeData)
        self._jgtradeapi_data_cb_ = OnTradeDataCallBack(OnRecvData)
        API_Start()

    def dlddata_by_acctidbymxz(self, acctidbybroker, accttype):
        # 账户类型调整: 现金账户 vs 保证金账户
        global g_serviceid
        if accttype in ['c']:
            g_serviceid = API_CreateService(TRADETYPE.TD_STOCK.value)
        elif accttype in ['m']:
            g_serviceid = API_CreateService(TRADETYPE.TD_CREDIT.value)
        else:
            raise ValueError('Unknown account type.')
        register_Linkcallback(g_serviceid, self._jgtradeapi_notice_cb_)
        register_Datacallback(g_serviceid, self._jgtradeapi_data_cb_)
        API_Connect(g_serviceid, c_char_p(b"124.74.252.82"), 8980, False)  # 此处传参： 交易服务器参数

        Login(acctidbybroker, '123321', g_serviceid)
        QryFund(g_serviceid)
        QryHold(g_serviceid)
        QryEntrust(g_serviceid)
        QryBusiness(g_serviceid)
        QryShortsell(g_serviceid)
        print(f'{acctidbybroker} trddata download finished.')

    def run(self):
        self.dlddata_by_acctidbymxz('0920111727', 'c')


        # iter_dict_acctinfo = self.col_acctinfo.find(
        #     {'DataDate': self.str_today, 'DataSourceType': 'hait_ehfz', 'DataDownloadMark': 1}
        # )
        # for dict_acctinfo in iter_dict_acctinfo:
        #     acctidbybroker = dict_acctinfo['AcctIDByBroker']
        #     accttype = dict_acctinfo['AcctType']
        #     self.dlddata_by_acctidbymxz(acctidbybroker, accttype)


if __name__ == '__main__':
    task = DldTrdDataFromEHFZApi()
    task.run()
















