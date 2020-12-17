#  coding:utf-8
"""python调用今古交易服务Dll库的数据结构定义声明文件"""
"""带@标注的字段请使用指定定义"""
from ctypes import *

# 响应信息
class JGtdcRspInfoField(Structure):
    _fields_ = [("nResultType", c_int),# @应答结果
                ("szErrorInfo", c_char * 128),  # 错误信息
                ("nFieldItem", c_int)]  # 应答数据个数

class JGtdcMachineInfo(Structure):
    _fields_ = [("szLocalIPAddr", c_char * 32),    # 本地IP
                ("szNetIPAddr", c_char * 32),       #  外网IP
                ("szMacAddr", c_char * 16),     # MAC地址
                ("szHDSequenceNo", c_char * 256),   # 硬盘序列号
                ("szCPUID", c_char * 128),      # CPUID
                ("szVersion", c_char * 16),     # 客户端版本号
                ("szQSID", c_char * 16)]        # 券商ID

# 用户登陆请求
class JGtdcReqUserLogin(Structure):
    _fields_ = [("cLoginType", c_char),              # @登陆校验类型
                ("nExchangeType", c_int),            # 市场类型 TJGtdcExchangeType
                ("szBranchNo", c_char * 8),          # 营业部号
                ("szLoginCode", c_char * 39),         # 登陆代码
                ("szLoginPassword", c_char * 32),    # 登陆密码
                ("szMACAddress", c_char * 16),       # MAC地址
                ("szIPAddress", c_char * 32),        # IP地址
                ("szMD5", c_char * 64)]              # MD5

# 用户登陆应答
class JGtdcRspUserLogin(Structure):
    _fields_ = [("szClientID", c_char * 16),         # 客户号
                ("nSubType", c_int),                 # 资金账号
                ("nSubDataType", c_int)]             # 支持的订阅类型

# 用户报单录入
class JGtdcReqOrderInsert(Structure):
    _fields_ = [("szClientID", c_char * 16),     # 客户号
                ("szBatchNo", c_char * 24),      # 批号
                ("szStockCode", c_char * 24),    # 证券代码
                ("nExchangeType", c_int),        # 市场类型 TJGtdcExchangeType
                ("nTradeType", c_int),           # @交易类型
                ("nPriceType", c_int),           # @价格类型
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong)]   # 委托价格

# 用户报单应答
class JGtdcRspOrderInsert(Structure):
    _fields_ = [("nResultType", c_int),  # @应答结果
                ("szErrorInfo", c_char * 128),  # 错误信息
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szBatchNo", c_char * 24),  # 批号
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szStockCode", c_char * 24),  # 证券代码
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("nTradeType", c_int),  # @交易类型
                ("nPriceType", c_int),  # @价格类型
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong)]  # 委托价格

# 用户撤单请求
class JGtdcReqOrderCancel(Structure):
    _fields_ = [("szClientID", c_char * 16),     # 客户号
                ("nExchangeType", c_int),        # 市场类型 TJGtdcExchangeType
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szBatchNo", c_char * 24)]  # 批号

# 用户撤单应答
class JGtdcRspOrderCancel(Structure):
    _fields_ = [("nResultType", c_int),  # @应答结果
                ("szErrorInfo", c_char * 128),  # 错误信息
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szNewEntrustNo", c_char * 24),  # 新合同号
                ("szBatchNo", c_char * 24)]  # 批号

# 投资者最大委托数查询
class JGtdcReqQryMax(Structure):
    _fields_ = [("szClientID", c_char * 16),     # 客户号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockCode", c_char * 24),  # 证券代码
                ("nTradeType", c_int),  # @交易类型
                ("nPriceType", c_int),  # @价格类型
                ("iEntrustPrice", c_longlong),  # 委托价格
                ("szBatchNo", c_char * 24)]      # 批号

# 投资者最大委托数应答
class JGtdcRspQryMax(Structure):
    _fields_ =[("szStockAccount", c_char * 16),  # 股东代码
               ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
               ("szStockCode", c_char * 24),  # 证券代码
               ("nTradeType", c_int),  # @交易类型
               ("nPriceType", c_int),  # @价格类型
               ("iEntrustPrice", c_longlong),  # 委托价格
               ("szBatchNo", c_char * 24),  # 批号
               ("iMaxAmount", c_longlong)]  # 最大可交易数量


# 投资者资金查询
class JGtdcReqQryFund(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("cMoneyType", c_char)]  # @币种


# 投资者资金查询应答
class JGtdcRspQryFund(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("cMoneyType", c_char),  # @币种
                ("cMainFlag", c_char),  # 主副标志
                ("dEnableBalance", c_double), # 可用余额
                ("dFetchBalance", c_double),  # 可取余额
                ("dFrozenBalance", c_double),  # 冻结金额
                ("dStockBalance", c_double),  # 证券市值
                ("dFundBalance", c_double),  # 资金余额
                ("dAssetBalance", c_double),  # 资产总值
                ("dInCome", c_double),  # 总盈亏
                ("dEnableBalanceHK", c_double)]  # 港股可用余额

# 投资者持仓查询
class JGtdcReqQryHold(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("szStockCode", c_char * 24),  # 证券代码
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("nQueryDirection", c_int),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串

# 投资者持仓查询应答
class JGtdcRspQryHold(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("cMoneyType", c_char),  # @币种
                ("iYdAmount", c_longlong),  # 昨日持仓量
                ("iStockAmount", c_longlong),  # 股份余额
                ("iEnableAmount", c_longlong),  # 可卖数量
                ("iPurchaseAmount", c_longlong),  # 可申购数量
                ("iPossessAmount", c_longlong),  # 当前拥股数量
                ("iFrozenAmount", c_longlong),  # 冻结数量
                ("iYStoreAmount", c_longlong),  # 昨日库存数量
                ("iCostPrice", c_longlong),  # 成本价格
                ("iKeepCostPrice", c_longlong),  # 保本价格
                ("dBuyCost", c_double),  # 当前成本
                ("dStockBalance", c_double),  # 证券市值
                ("dFloatIncome", c_double),  # 浮动盈亏
                ("dProIncome", c_double)]  # 累计盈亏

# 投资者当日委托查询
class JGtdcReqQryOrder(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("szStockCode", c_char * 24),  # 证券代码
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szEntrustNo", c_char * 24),  # 合同号
                ("nQueryDirection", c_int),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串

# 投资者当日委托查询应答
class JGtdcRspQryOrder(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szPositionStr", c_char * 40),  # 定位串
                ("szEntrustNo", c_char * 24),  # 合同号
                ("cMoneyType", c_char),  # @币种
                ("cEntrustStatus", c_char),  # @委托状态
                ("nTradeType", c_int),  # @交易类型
                ("nPriceType", c_int),  # @价格类型
                ("nEntrustDate", c_int),  # 委托日期
                ("nEntrustTime", c_int),  # 委托时间
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong),  # 委托价格
                ("iBusinessAmount", c_longlong),  # 成交数量
                ("iBusinessPrice", c_longlong),  # 成交价格
                ("iCancelAmount", c_longlong),  # 撤销数量
                ("dBusinessBalance", c_double),  # 成交金额
                ("nServiceType", c_int)]        # 业务类型

# 投资者可撤单查询
class JGtdcReqQryCancel(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("szStockCode", c_char * 24),  # 证券代码
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szEntrustNo", c_char * 24),  # 合同号
                ("nQueryDirection", c_int),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串

# 投资者可撤单查询应答
class JGtdcRspQryCancel(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szPositionStr", c_char * 40),  # 定位串
                ("szEntrustNo", c_char * 24),  # 合同号
                ("cMoneyType", c_char),  # @币种
                ("cEntrustStatus", c_char),  # @委托状态
                ("nTradeType", c_int),  # @交易类型
                ("nPriceType", c_int),  # @价格类型
                ("nEntrustDate", c_int),  # 委托日期
                ("nEntrustTime", c_int),  # 委托时间
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong),  # 委托价格
                ("iBusinessAmount", c_longlong),  # 成交数量
                ("iBusinessPrice", c_longlong),  # 成交价格
                ("iCancelAmount", c_longlong),  # 撤销数量
                ("dBusinessBalance", c_double),  # 成交金额
                ("nServiceType", c_int)]        # 业务类型

# 投资者成交单查询
class JGtdcReqQryTrade(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("szStockCode", c_char * 24),  # 证券代码
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szEntrustNo", c_char * 24),  # 合同号
                ("nQueryDirection", c_int),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串

# 投资者成交单查询应答
class JGtdcRspQryTrade(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szPositionStr", c_char * 40),  # 定位串
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szBusinessNo", c_char * 24),  # 成交编号
                ("cMoneyType", c_char),  # @币种
                ("cBusinessStatus", c_char),  # @成交状态
                ("nTradeType", c_int),  # @交易类型
                ("nPriceType", c_int),  # @价格类型
                ("nBusinessDate", c_int),  # 成交日期
                ("nBusinessTime", c_int),  # 成交时间
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong),  # 委托价格
                ("iBusinessAmount", c_longlong),  # 成交数量
                ("iBusinessPrice", c_longlong),  # 成交价格
                ("iCancelAmount", c_longlong),  # 撤销数量
                ("dBusinessBalance", c_double)]  # 成交金额

# 投资者直接还券
class JGtdcReqStockBack(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nExchangeType", c_int),     # 市场类型 TJGtdcExchangeType
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("szBatchNo", c_char * 24),      # 批号
                ("cStockBackMode", c_char),  # @还券模式
	            ("iEntrustAmount", c_longlong)]  # 委托数量
# 投资者直接还券应答
class JGtdcRspStockBack(Structure):
    _fields_ = [("nResultType", c_int),  # @应答结果
	            ("szErrorInfo", c_char * 128),  # 错误信息
	            ("szEntrustNo", c_char * 24),  # 合同号
	            ("szBatchNo", c_char * 24),      # 批号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockAccount", c_char * 16),  # 股东代码
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("cStockBackMode", c_char),  # @还券模式
	            ("iEntrustAmount", c_longlong)]  # 委托数量

# 投资者直接还款
class JGtdcReqMoneyBack(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
	            ("cMoneyType", c_char),  # @币种
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("cPayBackMode", c_char),   # @还款模式
                ("dPayBackBalance",c_double)]	# 还款金额


# 投资者直接还款应答
class JGtdcRspMoneyBack(Structure):
    _fields_ = [("nResultType", c_int),  # @应答结果
	            ("szErrorInfo", c_char * 128),  # 错误信息
	            ("szEntrustNo", c_char * 24),  # 合同号
	            ("cMoneyType", c_char),  # @币种
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockAccount", c_char * 16),  # 股东代码
	            ("cPayBackMode", c_char),   # 还款模式
	            ("dPayBackBalance",c_double)]	# 还款金额


# 投资者可融券卖出数量查询
class JGtdcReqQryMaxLoan(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
	            ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("nQueryAmount", c_int)]  # 查询数量



# 投资者可融券卖出数量查询应答
class JGtdcRspQryMaxLoan(Structure):
    _fields_ = [("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("szStockName", c_char * 24),  # 证券名称
                ("iMaxLoanAmount", c_longlong)]  # 可融券数量


# 投资者信用资产查询
class JGtdcReqQryAssets(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
	            ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
	            ("cMoneyType", c_char)]  # @币种


# 投资者信用资产查询应答
class JGtdcRspQryAssets(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
	            ("szClientID", c_char * 16),  # 客户号
	            ("szFundAccount", c_char * 16),  # 资金帐号
	            ("cMoneyType", c_char),  # @币种
                ("dEnableBalance", c_double),  # 可用余额
                ("dFetchBalance", c_double),  # 可取余额
                ("dFrozenBalance", c_double),  # 冻结金额
                ("dStockBalance", c_double),  # 证券市值
                ("dFundBalance", c_double), # 资金余额
                ("dAssetBalance", c_double),  # 资产总值
                ("dIncome", c_double),  # 总盈亏
                ("dEnableBail", c_double),  # 可用保证金
                ("dCreditQuota", c_double),  # 授信额度
                ("dFinanceQuota", c_double),  # 可融资金
                ("dShortsellQuota", c_double),	 # 可融券额度
                ("dAssureRatio", c_double),  # 维持担保比例
                ("dTotalDebit", c_double),  # 总负债
                ("dFundDebit", c_double),  # 资金负债
                ("dStockDebit", c_double),  # 股票负债
                ("dMustBackBalance", c_double)]  # 应还金额

# 投资者融资状况查询
class JGtdcReqQryFinance(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("cDebitStatus", c_char),  # @负债现状
                ("nStartDate", c_int),  # 起始日期
                ("nEndDate", c_int)]  # 结束日期

# 投资者融资状况查询应答
class JGtdcRspQryFinance(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
	            ("szClientID", c_char * 16),  # 客户号
	            ("szFundAccount", c_char * 16),  # 资金帐号
	            ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("szStockName", c_char * 24),  # 证券名称
	            ("szEntrustNo", c_char * 24),  # 报盘合同号
	            ("cMoneyType", c_char),  # @币种
	            ("cDebitStatus", c_char),  # @负债现状
                ("nOccurDate", c_int),  # 发生日期
                ("iOccurAmount", c_longlong),  # (买入数量)融资
                ("dOccurBalance", c_double),  # 发生金额  融资
                ("iBackAmount", c_longlong),  # 归还数量  融资
                ("dBackBalance", c_double)] # 归还金额  融资


# 投资者融券状况查询
class JGtdcReqQryShortsell(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockCode", c_char * 24),  # 证券代码
                ("cDebitStatus", c_char),  # @负债现状
                ("nStartDate", c_int),  # 起始日期
                ("nEndDate", c_int)]  # 结束日期


# 投资者融券状况查询应答
class JGtdcRspQryShortsell(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szEntrustNo", c_char * 24),  # 合同号
                ("cMoneyType", c_char),  # @币种
                ("cDebitStatus", c_char),  # @负债现状
                ("nOccurDate", c_int),  # 发生日期
                ("iOccurAmount", c_longlong),  # (买入数量)融资  # todo to check, 注释错误
                ("dOccurBalance", c_double),  # 发生金额  融资  # todo to check, 注释错误
                ("iBackAmount", c_longlong),  # 归还数量  融资  # todo to check, 注释错误
                ("dBackBalance", c_double)]  # 归还金额  融资  # todo to check, 注释错误

# 担保品划转
class JGtdcReqMortgageTrans(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
	            ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("szBatchNo", c_char * 24),      # 批号
	            ("nTradeType", c_int),           # @交易类型
	            ("iEntrustAmount", c_longlong),  # 委托数量
                ("szOtherFundAccount", c_char * 16),  # 对方资金账号
                ("szOtherStockAccount", c_char * 16),  # 对方股东代码
                ("szOtherSeatNo", c_char * 32)]  # 对方席位号

# 担保品划转应答
class JGtdcRspMortgageTrans(Structure):
    _fields_ = [("nResultType", c_int),  # @应答结果
	            ("szErrorInfo", c_char * 128),  # 错误信息
	            ("szEntrustNo", c_char * 24),  # 合同号
	            ("szBatchNo", c_char * 24),      # 批号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockAccount", c_char * 16),  # 股东代码
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("nTradeType", c_int),           # @交易类型
	            ("iEntrustAmount", c_longlong),  # 委托数量
                ("szOtherFundAccount", c_char * 16),  # 对方资金账号
                ("szOtherStockAccount", c_char * 16)]  # 对方股东代码


# 标的券查询
class  JGtdcReqQryObject(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
	            ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("nQueryDirection", c_int),  # @查询方向
	            ("nQueryAmount", c_int),  # 查询数量
	            ("szPositionStr", c_char * 40)]  # 定位串


# 标的券查询应答
class JGtdcRspQryObject(Structure):
    _fields_ = [("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockCode", c_char * 24),  # 证券代码
	            ("szStockName", c_char * 24),  # 证券名称
	            ("szPositionStr", c_char * 40),  # 定位串
                ("nObjectRights", c_int),			# @标的权限（按位）
                ("dFinanceBailRatio", c_double),  # 融资保证金比例
                ("dShortsellBailRatio", c_double),  # 融券保证金比例
                ("dMortgageRatio", c_double)]  # 担保品折算率



# 查询信用账户与普通账户对应关系
class JGtdcReqQryAccMatch(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMark", c_int),  # 查询标志
	            ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
	            ("szStockAccount", c_char * 16)]  # 股东代码


# 查询信用账户与普通账户对应关系应答
class JGtdcRspQryAccMatch(Structure):
    _fields_ = [("szClientName", c_char * 24),  # 客户姓名
                ("nCertType", c_int),  # 证件类型
                ("szCertCode", c_char * 50),  # 证件号码
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szCreditBranchNo", c_char * 8),  # 信用营业部号
                ("szCreditFundAccount", c_char * 16),  # 信用资金帐号
                ("szCreditHolderAccount", c_char * 16),  # 信用股东帐户
                ("szStockBranchNo", c_char * 8),  # 普通营业部号
                ("szStockFundAccount", c_char * 16),  # 普通资金帐号
                ("szStockHolderAccount", c_char * 16),  # 普通股东帐户
                ("szStockSeatNo", c_char * 32)]  # 普通帐户席位


#投资者期权委托下单
class JGtdcOptionReqEntrust(Structure):
    _fields_ = [("szClientID", c_char * 16),        # 客户号
	            ("nExchangeType", c_int),           # @市场类型
	            ("szStockAccount", c_char * 16),    # 股东代码
                ("szSeatNo", c_char * 32),          # 席位号
                ("szContractNumber", c_char * 16),	# 合约编码
	            ("szBatchNo", c_char * 24),         # 批号
                ("nTradeType", c_int),              # @交易类型
	            ("cOffsetType", c_char),            # @开平仓类型
                ("cCoveredType", c_char),           # @备兑标识
	            ("nPriceType", c_int),              # @价格类型
	            ("iEntrustAmount", c_longlong),     # 委托数量
                ("iEntrustPrice", c_longlong), ]    # 委托价格

#投资者期权委托下单应答
class JGtdcOptionRspEntrust(Structure):
    _fields_ = [("ResultType",	c_int),			    # @应答结果
                ("szErrorInfo",	c_char * 128),	    # 错误信息
	            ("szEntrustNo", c_char * 24),       # 合同号
	            ("szBatchNo", c_char * 24),         # 批号
                ("nExchangeType", c_int),           # @市场类型
                ("szStockAccount", c_char * 16),    # 股东代码
                ("szContractNumber", c_char * 16),  # 合约编码
                ("nTradeType", c_int),              # @交易类型
	            ("cOffsetType", c_char),            # @开平仓类型
	            ("cCoveredType", c_char),           # @备兑标识
	            ("nPriceType", c_int),              # @价格类型
                ("iEntrustAmount", c_longlong),     # 委托数量
                ("iEntrustPrice", c_longlong)]     # 委托价格

# 投资者期权撤单请求
class JGtdcOptionReqCancel(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szReportNo", c_char * 24),  # 申报号
                ("szBatchNo", c_char * 24),  # 批号
                ("nTradeType", c_int),  # @交易类型
                ("cOffsetType", c_char),  # @开平仓类型
                ("cCoveredType", c_char),  # @备兑标识
                ("nPriceType", c_int),  # @价格类型
                ("nEntrustDate", c_int),  # 委托日期
                ("nEntrustTime", c_int),  # 委托时间
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong),  # 委托价格
                ("iBusinessAmount", c_longlong)]  # 成交数量

# 投资者期权撤单应答
class JGtdcOptionRspCancel(Structure):
    _fields_ = [("nResultType", c_int),  # @应答结果
                ("szErrorInfo", c_char * 128),  # 错误信息
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szNewEntrustNo", c_char * 24),  # 新合同号
                ("szBatchNo", c_char * 24)]  # 批号

#投资者期权资金查询
class JGtdcOptionReqQryFund(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # @查询模式 TJGtdcQueryMode
                ("cMoneyType", c_char)]  # @币种

#投资者期权资金查询应答
class JGtdcOptionRspQryFund(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("cMoneyType", c_char),  # @币种
                ("cMainFlag", c_char),  # 主副标志
                ("dEnableBalance", c_double), # 可用余额
                ("dFetchBalance", c_double),  # 可取余额
                ("dFrozenBalance", c_double),  # 冻结金额
                ("dStockBalance", c_double),  # 证券市值
                ("dFundBalance", c_double),  # 资金余额
                ("dAssetBalance", c_double),  # 资产总值
                ("dInCome", c_double),  # 总盈亏
                ("dEnableBail", c_double),           # 可用保证金
                ("dUsedBail", c_double),           # 已用保证金
                ("dAgreeAssureRatio", c_double),   # 履约担保比例
                ("dRiskRatio", c_double),           # 风险度
                ("dRiskRatio1",  c_double)]        # 风险度1

# 投资者期权持仓查询
class JGtdcOptionReqQryHold(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # @查询模式
                ("szContractNumber", c_char * 16),  # 合约编码
                ("nExchangeType", c_int),  # @市场类型
                ("cQueryDirection", c_char),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szStockAccount", c_char * 16),  # 股东代码
                ("cOptionHoldType", c_char),  # @期权持仓类别
                ("szPositionStr", c_char * 40)]  # 定位串


# 投资者期权持仓查询应答
class JGtdcOptionRspQryHold(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szContractCode", c_char * 24),  # 合约代码
                ("szContractName", c_char * 40),  # 合约名称
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szPositionStr", c_char * 40),  # 定位串
                ("cMoneyType", c_char),  # @币种
                ("cOptionType", c_char),   # @期权类别
                ("cOptionHoldType", c_char), # @期权持仓类别
                ("iOptionYDAmount", c_longlong),# 期权昨日余额
                ("iOptionAmount", c_longlong), # 期权余额
                ("iEnableAmount", c_longlong),  # 可卖数量
                ("iPossessAmount", c_longlong),  # 当前拥股数量
                ("iFrozenAmount", c_longlong),  # 冻结数量
                ("iUnFrozenAmount", c_longlong),  # 解冻数量
                ("iTransitAmount", c_longlong),  # 在途数量
                ("iTodayOpenAmount", c_longlong),  # 今日开仓量
                ("iTodayPayoffAmount", c_longlong),  # 今日平仓量
                ("dPremiumBalance", c_double),  # 权利金
                ("dBailBalance", c_double),  # 保证金
                ("iCostPrice", c_longlong),  # 成本价格
                ("dBuyCost", c_double),  # 当前成本
                ("dOptionBalance", c_double),  # 期权市值
                ("dHoldIncome", c_double),  # 持仓盈亏
                ("dPayoffIncome", c_double)]  # 平仓盈亏

# 投资者期权成交单查询
class JGtdcOptionReqQryBusByPos(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # @查询模式 TJGtdcQueryMode
                ("szStockCode", c_char * 24),  # 证券代码
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szStockAccount", c_char * 16),  # 股东代码
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szEntrustNo", c_char * 24),  # 合同号
                ("nQueryDirection", c_int),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串

# 投资者期权成交单查询应答
class JGtdcOptionRspQryBusByPos(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szContractCode", c_char * 24),  # 合约代码
                ("szContractName", c_char * 40),  # 合约名称
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szPositionStr", c_char * 40),  # 定位串
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szReportNo", c_char * 24),  # 申报号
                ("szBatchNo", c_char * 24),  # 批号
                ("szBusinessNo", c_char * 24),  # 成交编号
                ("cMoneyType", c_char),  # @币种
                ("cBusinessStatus", c_char),  # @成交状态
                ("nTradeType", c_int),  # @交易类型
                ("cOffsetType", c_char),  # @开平仓类型
                ("cCoveredType", c_char),  # @备兑标识
                ("nPriceType", c_int),  # @价格类型
                ("nBusinessDate", c_int),  # 成交日期
                ("nBusinessTime", c_int),  # 成交时间
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong),  # 委托价格
                ("iBusinessAmount", c_longlong),  # 成交数量
                ("iBusinessPrice", c_longlong),  # 成交价格
                ("iCancelAmount", c_longlong),  # 撤销数量
                ("dBusinessBalance", c_double)]  # 成交金额

# 投资者期权可撤单查询
class JGtdcOptionReqQryRevocEnt(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # @查询模式 TJGtdcQueryMode
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szStockCode", c_char * 24),  # 证券代码
                ("szEntrustNo", c_char * 24),  # 合同号
                ("cQueryDirection", c_char),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串

# 投资者期权可撤单查询应答
class JGtdcOptionRspQryRevocEnt(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szContractCode", c_char * 24),  # 合约代码
                ("szContractName", c_char * 40),  # 合约名称
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szPositionStr", c_char * 40),  # 定位串
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szReportNo", c_char * 24),  # 申报号
                ("szBatchNo", c_char * 24),  # 批号
                ("cMoneyType", c_char),  # @币种
                ("cEntrustStatus", c_char),  # @委托状态
                ("nTradeType", c_int),  # @交易类型
                ("cOffsetType", c_char),  # @开平仓类型
                ("cCoveredType", c_char),  # @备兑标识
                ("nPriceType", c_int),  # @价格类型
                ("nEntrustDate", c_int),  # 委托日期
                ("nEntrustTime", c_int),  # 委托时间
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong),  # 委托价格
                ("iBusinessAmount", c_longlong),  # 成交数量
                ("iBusinessPrice", c_longlong),  # 成交价格
                ("iCancelAmount", c_longlong),  # 撤销数量
                ("dBusinessBalance", c_double),  # 成交金额
                ("szInvalidReason", c_char * 64)] # 废单原因 ############

# 投资者期权当日委托查询
class JGtdcOptionReqQryEntrust(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # @查询模式 TJGtdcQueryMode
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szStockCode", c_char * 24),  # 证券代码
                ("szEntrustNo", c_char * 24),  # 合同号
                ("cQueryDirection", c_char),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串



# 投资者期权当日委托查询应答
class JGtdcOptionRspQryEntrust(Structure):
    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szSeatNo", c_char * 32),  # 席位号
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szContractCode", c_char * 24),  # 合约代码
                ("szContractName", c_char * 40),  # 合约名称
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szPositionStr", c_char * 40),  # 定位串
                ("szEntrustNo", c_char * 24),  # 合同号
                ("szReportNo", c_char * 24),  # 申报号
                ("szBatchNo", c_char * 24),  # 批号
                ("cMoneyType", c_char),  # @币种
                ("cEntrustStatus", c_char),  # @委托状态
                ("nTradeType", c_int),  # @交易类型
                ("cOffsetType", c_char),  # @开平仓类型
                ("cCoveredType", c_char),  # @备兑标识
                ("nPriceType", c_int),  # @价格类型
                ("nEntrustDate", c_int),  # 委托日期
                ("nEntrustTime", c_int),  # 委托时间
                ("iEntrustAmount", c_longlong),  # 委托数量
                ("iEntrustPrice", c_longlong),  # 委托价格
                ("iBusinessAmount", c_longlong),  # 成交数量
                ("iBusinessPrice", c_longlong),  # 成交价格
                ("iCancelAmount", c_longlong),  # 撤销数量
                ("dBusinessBalance", c_double),  # 成交金额
                ("szInvalidReason", c_char * 64)]  # 废单原因 ############

# 投资者期权合约查询
class JGtdcOptionReqQryContract(Structure):
    _fields_ = [("szClientID", c_char * 16),  # 客户号
                ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szStockCode", c_char * 24),  # 证券代码
                ("cOptionType", c_char),  # 期权类别
                ("nQueryDirection", c_int),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串

# 投资者期权合约查询应答
class JGtdcOptionRspQryContract(Structure):
    _fields_ = [("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szContractNumber", c_char * 16),  # 合约编码
                ("szContractCode", c_char * 24),  # 合约代码
                ("szContractName", c_char * 40),  # 合约名称
                ("cOptionType", c_char),  # 期权类别
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("cOptionType", c_char),  # 证券类别
                ("szPositionStr", c_char * 40),  # 定位串
                ("cMoneyType", c_char),  # @币种
                ("nAmountMultiple", c_int),  # 合约乘数 #########################
                ("nOptionVersion", c_int),  # 期权版本  #########################
                ("nTradeBeginDate", c_int),  # 交易开始日期  ##################
                ("nTradeEndDate", c_int),  # 交易结束日期
                ("nExerciseBeginDate", c_int),  # 行权开始日期 ################
                ("nExerciseEndDate", c_int),  # 行权结束日期  #################
                ("iOptionPreClosePrice", c_longlong),  # 期权前收盘价格
                ("iStockPreClosePrice", c_longlong),  # 证券前收盘价格
                ("iOptionUpPrice", c_longlong),  # 期权涨停价格
                ("iOptionDownPrice", c_longlong),  # 期权跌停价格
                ("iExercisePrice", c_longlong),  # 行权价格
                ("dUnitBail", c_double),  # 单位保证金 ############
                ("iUnitBail", c_longlong),  # 市价单最大下单量
                ("iUnitBail", c_longlong),  # 市价单最小下单量
                ("iUnitBail", c_longlong),  # 限价单最大下单量
                ("iUnitBail", c_longlong),  # 限价单最小下单量
                ("cOptionStatus", c_char),  # 期权状态
                ("cOptionMode", c_char),    # 期权模式
                ("cOpenType", c_char),      # 开仓标识
                ("cSuspendedType", c_char), # 停牌标识
                ("cExpireType", c_char),    # 到期日标识
                ("cAdjustType", c_char) ]   # 调整标识

# 投资者备兑券持仓查询
class JGtdcOptionReqQryCoveredHold(Structure):
    _fields_ = [("szClientID", c_char * 16),     # 客户号
                ("nQueryMode", c_int),  # 查询模式 TJGtdcQueryMode
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szStockCode", c_char * 24),  # 证券代码
                ("nQueryDirection", c_int),  # @查询方向
                ("nQueryAmount", c_int),  # 查询数量
                ("szPositionStr", c_char * 40)]  # 定位串

# 投资者期权备兑持仓查询应答
class JGtdcOptionRspQryCoveredHold(Structure):

    _fields_ = [("szBranchNo", c_char * 8),  # 营业部号
                ("szClientID", c_char * 16),  # 客户号
                ("szFundAccount", c_char * 16),  # 资金帐号
                ("nExchangeType", c_int),  # 市场类型 TJGtdcExchangeType
                ("szStockAccount", c_char * 16),  # 股东代码
                ("szStockCode", c_char * 24),  # 证券代码
                ("szStockName", c_char * 24),  # 证券名称
                ("szPositionStr", c_char * 40),  # 定位串
                ("cMoneyType", c_char),  # @币种
	            ("iStockAmount", c_longlong),  # 股份余额
                ("iEnableAmount", c_longlong)]  # 可卖数量
