import pymongo

client_mongo = pymongo.MongoClient('mongodb://192.168.2.162:27017/')
db_basicinfo = client_mongo['basicinfo']
col_acctinfo = db_basicinfo['acctinfo']

list_dicts_acctinfo = list(col_acctinfo.find({'DataDate': '20201023'}))

print(list_dicts_acctinfo)







