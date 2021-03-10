import os
import shutil
from datetime import datetime
import time

from pymongo import MongoClient



def transfer_data(from_path, target_path, today_date):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for root, _, files in os.walk(from_path):
        for file in files:
            file_path = os.path.join(root + '/' + file)
            struct_time = time.localtime(os.stat(file_path).st_mtime)
            file_date = str(datetime(*struct_time[:3]).date()).replace('-', '')
            if file_date == today_date:
                # 是否taget_path有该dictionary
                dir_list = root.split('/')[-1].split('\\')[1:]
                path_1 = target_path
                if len(dir_list) != 0:
                    for i in range(len(dir_list)):
                        if not os.path.exists(os.path.join(path_1 + '/' + dir_list[i])):
                            os.mkdir(os.path.join(path_1 + '/' + dir_list[i]))
                            path_1 = os.path.join(path_1 + '/' + dir_list[i])
                        else:
                            path_1 = os.path.join(path_1 + '/' + dir_list[i])
                print(file, path_1)
                shutil.copy(file_path, path_1)


if __name__ == '__main__':
    str_today = datetime.today().strftime('%Y%m%d')
    server_mongodb = MongoClient(
        'mongodb://192.168.2.162:27017/', username='Maxincer', password='winnerismazhe'
    )
    db_global = server_mongodb['global']
    col_trdcalendar = db_global['trade_calendar']

    list_str_trdcalendar = []
    for _ in col_trdcalendar.find():
        list_str_trdcalendar += _['Data']
    idx_str_today = list_str_trdcalendar.index(str_today)
    str_last_trddate = list_str_trdcalendar[idx_str_today - 1]

    from_path = 'D:/data/trddata'
    target_path = f'D:/data/post_trade_data/{str_last_trddate}'
    transfer_data(from_path, target_path, str_last_trddate)
    print('Done')





