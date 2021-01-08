#!usr/bin/env/python38
# coding: utf-8
# Author: Maxincer
# CreateDateTime: 20201213193000

"""
从yh_apama 的ftp下载数据
每分钟最多查一笔
当日成交明细查询，每五分钟最多查一笔

"""

from datetime import datetime
import os
from threading import Thread
from time import sleep

import paramiko
from pymongo import MongoClient


class GetTrdDataFromApamaFTP:
    def __init__(self):
        self.host_apama = '139.196.103.39'
        self.port_apama = 22
        self.usrname = 'root'
        self.psw = 'llys3,ysykR'
        self.i_uniqueid = 0
        client_mongodb = MongoClient('mongodb://192.168.2.162:27017/', username='Maxincer', password='winnerismazhe')
        db_basicinfo = client_mongodb['basicinfo']
        self.col_acctinfo = db_basicinfo['acctinfo']
        self.list_dicts_acctinfo = list(
            self.col_acctinfo.find(
                {'DataDate': datetime.today().strftime("%Y%m%d"), 'DataSourceType': 'yh_apama', 'DataDownloadMark': 1}
            )
        )
        self.dirpath_output = 'D:/data/trddata/investment_manager_products/yh_apama'

    def generate_dat(self):
        """
        1. uniqueid, fundid, type
        2. 一种查询类型最多保持一行数据
        3. 当该行数据对应的请求编号比上一次请求编号大时，表示该类型是一笔新的查询
        """
        while True:
            for dict_acctinfo in self.list_dicts_acctinfo:
                acctidbybroker = dict_acctinfo['AcctIDByBroker']
                acctid_apama = dict_acctinfo['DownloadDataFilter']
                dirpath_local = f'data/{acctid_apama}' ''
                if not os.path.exists(dirpath_local):
                    os.mkdir(dirpath_local)
                fn_dat_query = f'query_{datetime.today().strftime("%Y%m%d")}.dat'
                fpath_dat_query = os.path.join(dirpath_local, fn_dat_query)
                with open(fpath_dat_query, 'w') as f:
                    self.i_uniqueid += 1
                    str_dat_query_content = f'{self.i_uniqueid}|{acctidbybroker}|1|\n'
                    self.i_uniqueid += 1
                    str_dat_query_content += f'{self.i_uniqueid}|{acctidbybroker}|2|\n'
                    self.i_uniqueid += 1
                    str_dat_query_content += f'{self.i_uniqueid}|{acctidbybroker}|3|\n'
                    f.write(str_dat_query_content)

                fn_dat_file_server_list = f'file_server_list_{datetime.today().strftime("%Y%m%d")}.dat'
                fpath_dat_file_server_list = os.path.join(dirpath_local, fn_dat_file_server_list)
                with open(fpath_dat_file_server_list, 'w') as f:
                    str_datetime = datetime.today().strftime('%H%M%S')
                    str_dat_file_server_list = f"{fn_dat_query}|{str_datetime}\n"
                    f.write(str_dat_file_server_list)
            sleep(30)

    def upload_dat(self):
        # upload
        trans = paramiko.Transport((self.host_apama, self.port_apama))
        trans.connect(username=self.usrname, password=self.psw)
        sftp = paramiko.SFTPClient.from_transport(trans)
        while True:
            for dict_acctinfo in self.list_dicts_acctinfo:
                acctidbymxz = dict_acctinfo['AcctIDByMXZ']
                fn_dat_query = f'query_{datetime.today().strftime("%Y%m%d")}.dat'
                acctid_apama = dict_acctinfo['DownloadDataFilter']
                dirpath_local = f'data/{acctid_apama}'
                fpath_local_dat_query = os.path.join(dirpath_local, fn_dat_query)

                dirpath_remote = f'//home/{acctid_apama}'
                fpath_remote_dat_query = f"{dirpath_remote}/{fn_dat_query}"
                fn_dat_file_server_list = f'file_server_list_{datetime.today().strftime("%Y%m%d")}.dat'
                fpath_remote_dat_file_server_list = f"{dirpath_remote}/{fn_dat_file_server_list}"
                fpath_local_dat_file_server_list = os.path.join(dirpath_local, fn_dat_file_server_list)
                sftp.put(fpath_local_dat_query, fpath_remote_dat_query)
                sleep(0.005)
                sftp.put(fpath_local_dat_file_server_list, fpath_remote_dat_file_server_list)
                print(f'{acctidbymxz} upload finished.')
            sleep(30)

    @staticmethod
    def remote_exist(sftp, path):
        try:
            sftp.stat(path)
        except IOError as e:
            if 'No such file' in str(e):
                return False
            raise
        else:
            return True

    def dld_dat(self):
        # download rawdata: stock, query, dealdetail
        trans = paramiko.Transport((self.host_apama, self.port_apama))
        trans.connect(username=self.usrname, password=self.psw)
        sftp = paramiko.SFTPClient.from_transport(trans)
        while True:
            for dict_acctinfo in self.list_dicts_acctinfo:
                acctidbymxz = dict_acctinfo['AcctIDByMXZ']
                fn_dat_fund = f'fund_{datetime.today().strftime("%Y%m%d")}.dat'
                fn_dat_stock = f'stock_{datetime.today().strftime("%Y%m%d")}.dat'
                fn_dat_dealdetail = f'dealdetail_{datetime.today().strftime("%Y%m%d")}.dat'
                acctid_apama = dict_acctinfo['DownloadDataFilter']
                dirpath_local = f'{self.dirpath_output}/{acctid_apama}'
                if not os.path.exists(dirpath_local):
                    os.mkdir(dirpath_local)
                dirpath_remote = f'//home/{acctid_apama}'
                fpath_local_dat_fund = os.path.join(dirpath_local, fn_dat_fund)
                fpath_local_dat_stock = os.path.join(dirpath_local, fn_dat_stock)
                fpath_local_dat_dealdetail = os.path.join(dirpath_local, fn_dat_dealdetail)

                fpath_remote_dat_fund = f"{dirpath_remote}/{fn_dat_fund}"
                fpath_remote_dat_stock = f"{dirpath_remote}/{fn_dat_stock}"
                fpath_remote_dat_dealdetail = f"{dirpath_remote}/{fn_dat_dealdetail}"

                if self.remote_exist(sftp, fpath_remote_dat_fund):
                    sftp.get(fpath_remote_dat_fund, fpath_local_dat_fund)
                    print(f'{acctidbymxz} download finished.')

                if self.remote_exist(sftp, fpath_remote_dat_stock):
                    sftp.get(fpath_remote_dat_stock, fpath_local_dat_stock)
                    print(f'{acctidbymxz} download finished.')

                if self.remote_exist(sftp, fpath_remote_dat_dealdetail):
                    sftp.get(fpath_remote_dat_dealdetail, fpath_local_dat_dealdetail)
                    print(f'{acctidbymxz} download finished.')

            sleep(30)

    def run(self):
        thread_generate_dat = Thread(target=self.generate_dat)
        thread_generate_dat.start()
        thread_upload_dat = Thread(target=self.upload_dat)
        thread_upload_dat.start()
        thread_dld_dat = Thread(target=self.dld_dat)
        thread_dld_dat.start()


if __name__ == '__main__':
    task = GetTrdDataFromApamaFTP()
    task.run()



















