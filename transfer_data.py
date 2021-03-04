import os
import shutil
import datetime
import time


def transfer_data(from_path, target_path, today_date):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for root, _, files in os.walk(from_path):
        for file in files:
            file_path = os.path.join(root + '/' + file)
            struct_time = time.localtime(os.stat(file_path).st_mtime)
            file_date = str(datetime.datetime(*struct_time[:3]).date()).replace('-', '')
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
    today_date = str(datetime.datetime.today().date()).replace('-', '')
    # today_date = '20210223'
    from_path = 'D:/data/trddata'
    target_path = f'D:/data/post_trade_data/{today_date}'
    transfer_data(from_path, target_path, today_date)
    print('Done')





