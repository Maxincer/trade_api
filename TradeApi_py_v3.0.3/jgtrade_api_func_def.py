#!/usr/bin/env python
#  coding:utf-8
"""python调用今古交易服务Dll库函数声明文件"""
from ctypes import *

# 声明回调函数
OnTradeLinkCallBack = WINFUNCTYPE(None, c_uint, c_int, c_char_p)
OnTradeDataCallBack = WINFUNCTYPE(None, c_uint, c_int, c_void_p, c_int, c_void_p, c_int)
OnTradePushDataCallBack = WINFUNCTYPE(None, c_uint, c_int, c_void_p, c_int)


# 加载c格式的dll动态库
jgtradeapi = windll.LoadLibrary(r'D:\projects\TradeApi_py_v3.0.3\JGTradeApi.dll')

# 设置调用api的返回值和参数

# 初始化交易服务
jgtradeapi.TRADEAPI_Start.restype = c_bool
jgtradeapi.TRADEAPI_Start.argtypes = []

# 停止交易服务
jgtradeapi.TRADEAPI_Stop.restype = c_bool
jgtradeapi.TRADEAPI_Stop.argtypes = []

# 创建服务
jgtradeapi.TRADEAPI_CreateService.restype = c_uint
jgtradeapi.TRADEAPI_CreateService.argtypes = [c_int]

# 注册连接通知回调
jgtradeapi.TRADEAPI_RegisterLinkCallback.restype = c_bool
jgtradeapi.TRADEAPI_RegisterLinkCallback.argtypes = [c_uint, c_void_p]

# 注册业务数据回调
jgtradeapi.TRADEAPI_RegisterDataCallback.restype = c_bool
jgtradeapi.TRADEAPI_RegisterDataCallback.argtypes = [c_uint, c_void_p]

# 注册业务主推数据回调
jgtradeapi.TRADEAPI_RegisterPushDataCallback.restype = c_bool
jgtradeapi.TRADEAPI_RegisterPushDataCallback.argtypes = [c_uint, c_void_p]

#连接服务器
jgtradeapi.TRADEAPI_ConnectService.restype = c_bool
jgtradeapi.TRADEAPI_ConnectService.argtypes = [c_uint, c_char_p, c_ushort, c_bool]

# 断开服务器
jgtradeapi.TRADEAPI_DisconnectService.restype = c_bool
jgtradeapi.TRADEAPI_DisconnectService.argtypes = [c_uint]


# 业务请求
jgtradeapi.TRADEAPI_Send.restype = c_int
jgtradeapi.TRADEAPI_Send.argtypes = [c_uint, c_int, c_char_p, c_int, c_int]