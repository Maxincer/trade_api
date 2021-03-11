#!usr/bin/env/python38
# coding: utf-8
# Author: Maxincer
# CreateDateTime: 20210311133000

"""
备份清算后数据
当前算法：
    1. 根据文件修改时间生成清算数据的原始硬文件, 筛选时间: T+1日00:00 - T+1日9:15， 生成T日的清算数据文件
    2. 需要转移的文件为: [fund.csv, holding.csv, short_position.csv]
    3. 在路径中增加 T-1, T, T+1 设计, 其中T日的意思为交易数据对应的交易日期。
    即： 在T+1日盘前运行此程序，将T+1日生成的数据文件存入T日的清算数据地址中；数据文件名不变，其中的日期仍为T+1。
"""

import os
import shutil
from datetime import datetime
import time

from pymongo import MongoClient


class GeneratePostTradeData:
    def __init__(self):
        self.dt_today = datetime.today()
        self.str_today = self.dt_today.strftime('%Y%m%d')
        server_mongodb = MongoClient(
            'mongodb://192.168.2.162:27017/', username='Maxincer', password='winnerismazhe'
        )
        db_global = server_mongodb['global']
        col_trdcalendar = db_global['trade_calendar']

        list_str_trdcalendar = []
        for _ in col_trdcalendar.find():
            list_str_trdcalendar += _['Data']
        idx_str_today = list_str_trdcalendar.index(self.str_today)
        self.str_last_trddate = list_str_trdcalendar[idx_str_today - 1]
        
        self.dirpath_from = 'D:/data/trddata'
        self.dirpath_to = f'D:/data/post_trade_data/{self.str_last_trddate}'

    def transfer_data(self):
        if not os.path.exists(self.dirpath_to):
            os.mkdir(self.dirpath_to)

        for root, _, files in os.walk(self.dirpath_from):
            for file in files:
                file_path = os.path.join(root + '/' + file)
                struct_time = time.localtime(os.stat(file_path).st_mtime)
                file_date = str(datetime(*struct_time[:3]).date()).replace('-', '')
                if file_date == self.str_today:
                    dir_list = root.split('/')[-1].split('\\')[1:]
                    path_1 = self.dirpath_to
                    if len(dir_list) != 0:
                        for i in range(len(dir_list)):
                            if not os.path.exists(os.path.join(path_1 + '/' + dir_list[i])):
                                os.mkdir(os.path.join(path_1 + '/' + dir_list[i]))
                                path_1 = os.path.join(path_1 + '/' + dir_list[i])
                            else:
                                path_1 = os.path.join(path_1 + '/' + dir_list[i])
                    print(f'已生成{file}到{path_1}中。')
                    shutil.copy(file_path, path_1)

    def run(self):
        self.transfer_data()


if __name__ == '__main__':
    task = GeneratePostTradeData()
    task.run()
    print('Done')





