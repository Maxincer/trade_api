# coding:utf-8
"""python调用今古交易服务Dll库的api接口文件"""
from api_hait_ehfz.jgtrade_api_func_def import *
from api_hait_ehfz.jgtrade_api_data_def import *  # 隐式调用了该文件中的参数，不可删除
from api_hait_ehfz.jgtrade_api_struct_def import *


# 初始化交易服务
# @type service_id 服务ID,由API_CreateService返回值
# @return  True表示初始化交易服务成功，False表示失败
def API_Start():
    if ( True == jgtradeapi.TRADEAPI_Start()):
        print("API初始化服务成功")
    else:
        print("API初始化服务失败")

# 停止交易服务
# @type service_id 服务ID,由API_CreateService返回值
# @return  True表示停止交易服务成功，False表示失败
def API_Stop():
    if ( True == jgtradeapi.TRADEAPI_Stop()):
        print("API停止交易服务成功")
    else:
        print("API停止交易服务失败")


# 创建服务
# @service_type  创建服务类型
# @return  返回service_id
def API_CreateService(service_type):
    service_id = jgtradeapi.TRADEAPI_CreateService(service_type)
    if( 0 <= service_id):
        print("创建服务成功")
    else:
        print("创建服务失败")
    return  service_id

# 断开服务器
# @type service_id 服务ID,由API_CreateService返回值
# @return  True表示断开服务器成功，False表示失败
def API_DisConnect(service_id):
    if ( True == jgtradeapi.TRADEAPI_DisconnectService(service_id)):
        print("API断开服务器成功")
    else:
        print("API断开服务器失败")


# 连接服务器
# @type service_id 服务ID,由API_CreateService返回值
# @return  True表示连接服务器成功，False表示失败
def API_Connect(service_id, address, port, domain):
    if ( True == jgtradeapi.TRADEAPI_ConnectService(service_id, address, port, domain)):
        print("API连接服务器成功")
    else:
        print("API连接服务器失败")


# 注册连接回调函数
# @type service_id 服务ID,由API_CreateService返回值
# @func 回调函数对象
# @return  True表示注册成功，False表示失败
def register_Linkcallback(service_id, func):
    jgtradeapi.TRADEAPI_RegisterLinkCallback(service_id, func)


# 注册业务回调函数
# @type service_id 服务ID,由API_CreateService返回值
# @func 回调函数对象
# @return  True表示注册成功，False表示失败
def register_Datacallback(service_id, func):
    jgtradeapi.TRADEAPI_RegisterDataCallback(service_id, func)


# 注册业务主推回调函数
# @type service_id 服务ID,由API_CreateService返回值
# @func 回调函数对象
# @return  True表示注册成功，False表示失败
def register_PushDatacallback(service_id, func):
    jgtradeapi.TRADEAPI_RegisterPushDataCallback(service_id, func)


# 业务请求
# @type service_id 服务ID,由API_CreateService返回值
# @funcid  功能ID
# @req_data 请求结构体地址
# @req_item 请求数据个数
# @requestid 请求id
# @return  大于等于0表示成功，负数表示失败
def API_TradeSend(service_id, funcid, req_data, req_item, requestid):
    if 0 <= jgtradeapi.TRADEAPI_Send(service_id, funcid, req_data, req_item, requestid):
        print("调用业务请求接口成功")
        return 0
    else:
        print("调用业务请求接口失败")
        return -1

