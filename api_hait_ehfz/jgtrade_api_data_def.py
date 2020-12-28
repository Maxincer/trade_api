#  coding:utf-8
"""python调用今古交易服务Dll库的数据结构声明文件"""
from enum import Enum


class TRADETYPE(Enum):
    TD_STOCK = 1000                         # 股票
    TD_CREDIT = 2000                         # 信用
    TD_FUTURE = 3000                         # 期货
    TD_OPTION = 4000                         # 期权

class LINK_NOTICE_TYPE(Enum):
    LINK_NOTICE_TYPE_NULL = -1               # 无
    LINK_NOTICE_TYPE_CONNECTING = 0          # 正在连接
    LINK_NOTICE_TYPE_CONNECTE_SUCCESSED = 2  # 连接成功
    LINK_NOTICE_TYPE_CONNECTE_FAILED = 3     # 连接失败
    LINK_NOTICE_TYPE_DISCONNECTED = 4        # 连接断开
    LINK_NOTICE_TYPE_ERRORINFO = 5           # 错误信息


class TRADE_FUNCID_TYPE(Enum):
    JG_FUNCID_TRD_MACHINEINFO = 110000      # 设置用户机器信息
    JG_FUNCID_STOCK_Login = 110100          # 账号登陆
    JG_FUNCID_STOCK_Logout = 110101         # 账号退出
    JG_FUNCID_STOCK_Entrust = 110102        # 委托下单
    JG_FUNCID_STOCK_Cancel = 110103         # 委托撤单
    JG_FUNCID_STOCK_QryMax = 110104         # 最大交易数量查询
    JG_FUNCID_STOCK_QryFund = 110105        # 资金查询
    JG_FUNCID_STOCK_QryHold = 110106        # 持仓查询
    JG_FUNCID_STOCK_QryEntrust = 110107     # 当日委托查询
    JG_FUNCID_STOCK_QryRevocEnt = 110108    # 可撤单查询
    JG_FUNCID_STOCK_QryBusByPos = 110109    # 增量成交查询

    JG_FUNCID_CREDIT_Login = 110100  # 账号登陆
    JG_FUNCID_CREDIT_Logout = 110101  # 账号退出
    JG_FUNCID_CREDIT_QryFund = 110105       # 资金查询
    JG_FUNCID_CREDIT_QryHold = 110106       # 持仓查询
    JG_FUNCID_CREDIT_QryBusByPos = 110109   # 增量成交查询
    JG_FUNCID_CREDIT_StockBack = 120200     # 直接还券
    JG_FUNCID_CREDIT_PayBack = 120201       # 直接还款
    JG_FUNCID_CREDIT_QryMaxLoan = 120301    # 可融券查询
    JG_FUNCID_CREDIT_QryAssets = 120302     # 信用资产查询
    JG_FUNCID_CREDIT_QryFinance = 120303    # 融资状况查询
    JG_FUNCID_CREDIT_QryShortsell = 120304  # 融券状况查询
    JG_FUNCID_CREDIT_QryAccMatch = 120606  # 查询信用账户与普通账户对应关系

    JG_FUNCID_FUTURE_Login                  = 130100	# 期货账号登陆
    JG_FUNCID_FUTURE_Logout	                = 130101	# 期货账号退出
    JG_FUNCID_FUTURE_QrySettlement          = 130120	# 期货账单查询
    JG_FUNCID_FUTURE_ConfirmSettle          = 130121	# 期货账单确认
    JG_FUNCID_FUTURE_QryContract            = 130122	# 期货合约查询
    JG_FUNCID_FUTURE_Entrust                = 130200	# 期货委托下单
    JG_FUNCID_FUTURE_Cancel					= 130201	# 期货委托撤单
    JG_FUNCID_FUTURE_QryMax					= 130202	# 期货最大交易数量查询
    JG_FUNCID_FUTURE_QryHolder				= 130300	# 期货交易编码查询
    JG_FUNCID_FUTURE_QryFund				= 130301	# 期货资金查询
    JG_FUNCID_FUTURE_QryHold				= 130302	# 期货持仓查询
    JG_FUNCID_FUTURE_QryEntrust				= 130303	# 期货当日委托查询
    JG_FUNCID_FUTURE_QryRevocEnt			= 130304	# 期货可撤单查询
    JG_FUNCID_FUTURE_QryBusByPos			= 130306	# 期货增量成交查询

    JG_FUNCID_OPTION_Login					= 140100	# 期权账号登陆
    JG_FUNCID_OPTION_Logout					= 140101	# 期权账号退出
    JG_FUNCID_OPTION_QryContract			= 140122	# 期权合约查询
    JG_FUNCID_OPTION_Entrust				= 140200	# 期权委托下单
    JG_FUNCID_OPTION_Cancel					= 140201	# 期权委托撤单
    JG_FUNCID_OPTION_QryMax					= 140202	# 期权最大交易数量查询
    JG_FUNCID_OPTION_CoveredTrans			= 140203	# 期权备兑证券划转
    JG_FUNCID_OPTION_QryCoveredMax			= 140204	# 期权备兑可划转数量查询
    JG_FUNCID_OPTION_QryFund				= 140301	# 期权资金查询
    JG_FUNCID_OPTION_QryHold				= 140302	# 期权持仓查-询
    JG_FUNCID_OPTION_QryEntrust				= 140303	# 期权当日委托查询
    JG_FUNCID_OPTION_QryRevocEnt			= 140304	# 期权可撤单查询
    JG_FUNCID_OPTION_QryBusByPos			= 140306	# 期权增量成交查询
    JG_FUNCID_OPTION_QryCoveredHold			= 140307	# 期权备兑券持仓查询
    JG_FUNCID_OPTION_QryExerciseAssign		= 140308	# 期权行权指派查询
    JG_FUNCID_OPTION_QryLackCoveredStock	= 140309	# 期权备兑证券不足查询
    JG_FUNCID_OPTION_QryFetchFund			= 140310	# 期权可取资金查询
    JG_FUNCID_OPTION_QryHisEntrust			= 140320	# 期权历史委托查询
    JG_FUNCID_OPTION_QryHisBusiness			= 140321	# 期权历史成交查询
    JG_FUNCID_OPTION_QryHisExerciseAssign	= 140322	# 期权历史行权指派查询
    JG_FUNCID_OPTION_AddAutoExercise		= 140500	# 期权增加自动行权
    JG_FUNCID_OPTION_ModAutoExercise		= 140501	# 期权修改自动行权
    JG_FUNCID_OPTION_DelAutoExercise		= 140502	# 期权删除自动行权
    JG_FUNCID_OPTION_QryAutoExercise		= 140503	# 期权自动行权查询
    JG_FUNCID_OPTION_QryCovered				= 140504	# 期权备兑证券查询
    JG_FUNCID_OPTION_QryHisHold				= 140505	# 期权昨日持仓查询
    JG_FUNCID_OPTION_QrySettlement			= 140506	# 期权结算单查询
    JG_FUNCID_OPTION_QryDelivery			= 140507	# 期权交割单查询
    JG_FUNCID_OPTION_TransferFund			= 140508	# 期权调拨资金
    JG_FUNCID_OPTION_ShareCombSplitEntrust	= 140509	# 期权个股组合拆分委托
    JG_FUNCID_OPTION_QryShareCombSplitHold	= 140510	# 期权个股组合持仓明细查询
    JG_FUNCID_OPTION_QryShareCombSplitLots	= 140511	# 期权个股可组合可拆分手数查询
    JG_FUNCID_OPTION_QryShareUserHisFundChange= 140512	# 期权个股客户资金变动流水历史查询
    JG_FUNCID_OPTION_SettlementConfrim		= 140516	# 期权结算单确认


# 登陆类型
JG_TDC_LOGINTYPE_FundAccount = '0'  # 资金账号
JG_TDC_LOGINTYPE_ClientID = '1'  # 客户号
JG_TDC_LOGINTYPE_StockAccount = '2'   # 股东代码
JG_TDC_LOGINTYPE_OnlyQuery = '3'  # 只做查询

# 市场类型
class TJGtdcExchangeType(Enum):
    JG_TDC_EXCHANGETYPE_SZA	=	1 # 深A
    JG_TDC_EXCHANGETYPE_SHA	=	2 # 沪A
    JG_TDC_EXCHANGETYPE_SZB	=	3 # 深B
    JG_TDC_EXCHANGETYPE_SHB	=	4 # 沪B
    JG_TDC_EXCHANGETYPE_TZA	=	5 # 特转A
    JG_TDC_EXCHANGETYPE_TZB	=	6 # 特转B
    JG_TDC_EXCHANGETYPE_OPTSZA	= 11 # 个股期权深A
    JG_TDC_EXCHANGETYPE_OPTSHA	= 12 # 个股期权沪A
    JG_TDC_EXCHANGETYPE_SHHK = 13 # 沪港通
    JG_TDC_EXCHANGETYPE_SZHK = 14 # 深港通
    JG_TDC_EXCHANGETYPE_CFFEX = 100 # 金融期货
    JG_TDC_EXCHANGETYPE_SHFE  =	101 # 上海商品期货
    JG_TDC_EXCHANGETYPE_CZCE   = 102 # 郑州商品期货
    JG_TDC_EXCHANGETYPE_DCE	= 103 # 大连商品期货


# 查询模式
class TJGtdcQueryMode(Enum):
    JG_TDC_QUERYMODE_All = 0  # 查询全部
    JG_TDC_QUERYMODE_ByFundAccount	=		1 # 按资金账号查询
    JG_TDC_QUERYMODE_ByExchange		=		2 # 按市场查询
    JG_TDC_QUERYMODE_ByCode			=		3 # 按证券代码或合约代码查询
    JG_TDC_QUERYMODE_ByEntrustNo	=		4 # 按委托合同号查询
    JG_TDC_QUERYMODE_ByMoneyType	=		5 # 按币种查询
    JG_TDC_QUERYMODE_ByDebitStatus	=		6 # 按负债现状查询
    JG_TDC_QUERYMODE_ByOptionNumber	=		7 # 按合约编码查询
    JG_TDC_QUERYMODE_ByOptionType	=		8 # 按期权类型查询
    JG_TDC_QUERYMODE_ByOptionHoldType	=	9 # 按期权持仓类别查询
    JG_TDC_QUERYMODE_ByComboID		=		10 # 按组合ID查询
    JG_TDC_QUERYMODE_ByBankCode		=		11 # 按银行代码查询
    JG_TDC_QUERYMODE_ByServerType	=		12 # 按服务器类型查询
    JG_TDC_QUERYMODE_BySubServerType	=	13 # 按服务器子类型查询
    JG_TDC_QUERYMODE_ByExerciseStrategyType	 = 14  # 按行权策略类型查询
    JG_TDC_QUERYMODE_ByTerminalType		=	15 # 按终端类型查询
    JG_TDC_QUERYMODE_BySubTerminalType	=	16 # 按终端子类型查询
    JG_TDC_QUERYMODE_ByPostionStr     =      17 # 按索引查询


# 查询方向
# 倒序（往后翻，查询更早的信息）
JG_TDC_QUERYDIRECTION_Inverted	= '0'
# 顺序（往前翻，查询更晚的信息）
JG_TDC_QUERYDIRECTION_Sequence	= '1'



# 委托状态
# 未报
JG_TDC_ENTRUSTSTATUS_NotReport		=	'0'
# 正报
JG_TDC_ENTRUSTSTATUS_Reporting		=	'1'
# 已报
JG_TDC_ENTRUSTSTATUS_Reported		=	'2'
# 已报待撤
JG_TDC_ENTRUSTSTATUS_Canceling		=	'3'
# 部成待撤
JG_TDC_ENTRUSTSTATUS_PartFilledCanceling =	'4'
# 部撤
JG_TDC_ENTRUSTSTATUS_PartFilledCanceled	 = '5'
# 已撤
JG_TDC_ENTRUSTSTATUS_Canceled		=	'6'
# 部成
JG_TDC_ENTRUSTSTATUS_PartFilled		=	'7'
# 已成
JG_TDC_ENTRUSTSTATUS_AllFilled		=	'8'
# 废单
JG_TDC_ENTRUSTSTATUS_Invalid		=	'9'
# 待报
JG_TDC_ENTRUSTSTATUS_Queueing		=	'a'
# 场内拒绝
JG_TDC_ENTRUSTSTATUS_Rejected		=	'b'


# 成交状态
# 普通成交
JG_TDC_BUSINESSSTATUS_Filled =	'0'
# 撤单成交
JG_TDC_BUSINESSSTATUS_Canceled = '1'
# 废单成交
JG_TDC_BUSINESSSTATUS_Invalid =	'2'


# 币种
# 人民币
JG_TDC_MONEYTYPE_RMB =	'0'
# 港币
JG_TDC_MONEYTYPE_HKD = 	'1'
# 美元
JG_TDC_MONEYTYPE_USD =	'2'



# 交易类型
# 普通买入
JG_TDC_TRADETYPE_Buy		=		   1
# 普通卖出
JG_TDC_TRADETYPE_Sell		=		   2
# ETF申购
JG_TDC_TRADETYPE_ETFApply	=		   3
# ETF赎回
JG_TDC_TRADETYPE_ETFRedeem	=		   4
# 跨市ETF申购
JG_TDC_TRADETYPE_ETFTranApply	=	   5
# 跨市ETF赎回
JG_TDC_TRADETYPE_ETFTranRedeem	=	   6
# 分级基金合并
JG_TDC_TRADETYPE_StructuredFundMarge =  7
# 分级基金拆分
JG_TDC_TRADETYPE_StructuredFundSplit =  8
# LOF申购
JG_TDC_TRADETYPE_LOFApply			=   9
# LOF赎回
JG_TDC_TRADETYPE_LOFRedeem			=   10
# 融资买入
JG_TDC_TRADETYPE_LoanBuy			=  11
# 融券卖出
JG_TDC_TRADETYPE_LoanSell		=	  12
# 买券还券
JG_TDC_TRADETYPE_EnBuyBack			=  13
# 卖券还款
JG_TDC_TRADETYPE_EnSellBack			=  14
# 直接还券
JG_TDC_TRADETYPE_StockBack			=  15
# 直接还款
JG_TDC_TRADETYPE_PayBack			=  16
# 担保品划入
JG_TDC_TRADETYPE_MortgageIn			=  21
# 担保品划出
JG_TDC_TRADETYPE_MortgageOut		=  22
# 认购行权
JG_TDC_TRADETYPE_CallExercise		=  31
# 认沽行权
JG_TDC_TRADETYPE_PutExercise		=  32
# 证券锁定
JG_TDC_TRADETYPE_StockLock			=  33
# 证券解锁
JG_TDC_TRADETYPE_StockUnLock		=  34
# 认购自动行权
JG_TDC_TRADETYPE_AutoCallExercise	 = 35
# 认沽自动行权
JG_TDC_TRADETYPE_AutoPutExercise	 = 36
# 跨境ETF申购
JG_TDC_TRADETYPE_ETFCrossApply		=  50
# 跨境ETF赎回
JG_TDC_TRADETYPE_ETFCrossRedeem		 = 51
# 货币基金申购
JG_TDC_TRADETYPE_MoneyFundApply		=  52
# 货币基金赎回
JG_TDC_TRADETYPE_MoneyFundRedeem	=  53
# 新股申购
JG_TDC_TRADETYPE_NewStockApply		=  60
# 配售申购
JG_TDC_TRADETYPE_ValueAllotApply	 = 61


# 价格类型
# 限价
JG_TDC_PRICETYPE_Limit		=	1
# 对方最优价格
JG_TDC_PRICETYPE_OtherBest	=	2
# 本方最优价格
JG_TDC_PRICETYPE_Best		=	3
# 即时成交剩余撤销
JG_TDC_PRICETYPE_Timely		=	4
# 最优五档剩余撤销
JG_TDC_PRICETYPE_BestOrCancel  = 5
# 全额成交或撤销
JG_TDC_PRICETYPE_FillOrCancel  = 6
# 最优五档剩余转限价
JG_TDC_PRICETYPE_BestOrLimit   = 7
# 市价剩余转限价
JG_TDC_PRICETYPE_MarketOrLimit = 8
# 全额即时限价
JG_TDC_PRICETYPE_FillOrLimit   = 9


# 还券模式
# 直接还券
JG_TDC_STOCKBACKMODE_Direct		= '0'
# 意向还券
JG_TDC_STOCKBACKMODE_Will		= '1'
# 即时还券
JG_TDC_STOCKBACKMODE_Immediate	= '2'


# 负债现状
# 未了结
JG_TRD_DEBITSTATUS_NotFinish	= '0'
# 已了结
JG_TRD_DEBITSTATUS_Finish		= '1'
# 到期未平仓
JG_TRD_DEBITSTATUS_DueNotPayOff	= '2'



# 标的权限（按位判断权限）
# 融资标的
JG_TRD_OBJECTRIGHTS_Finance		 = 0x01
# 融券标的
JG_TRD_OBJECTRIGHTS_Shortsell	 = 0x02
# 担保品标的
JG_TRD_OBJECTRIGHTS_Mortgage	 = 0x04


# 查询标记
# 信用账户查询普通账户
JG_TDC_QUERYMARK_Normal	  = 0
# 普通账户查询信用账户
JG_TDC_QUERYMARK_Credit	  = 1

# 应答结果
# 成功
JG_TDC_ANSRESULT_Success	=	0
# 柜台返回错误
JG_TDC_ANSRESULT_Error		=	-1



#开平仓类型
#开仓
JG_TDC_OFFSETTYPE_Open		  =	48
#平仓
JG_TDC_OFFSETTYPE_PayOff	  =	49
#平今仓
JG_TDC_OFFSETTYPE_PayOffToday =	50



#套保类型
#投机
JG_TDC_HEDGETYPE_Speculation =  0
#套利
JG_TDC_HEDGETYPE_Arbitrage	 =	1
#保值
JG_TDC_HEDGETYPE_Hedge		 =	2

#备兑标识
#非备兑
JG_TDC_COVEREDTYPE_No	=	48
#备兑
JG_TDC_COVEREDTYPE_Yes	=	49

#期权类别
#认购
JG_TDC_OPTIONTYPE_Call	=	'0'
#认沽
JG_TDC_OPTIONTYPE_Put	=	'1'

#证券类别
#股票
JG_TDC_STOCKTYPE_Stock	=	'0'
#ETF基金
JG_TDC_STOCKTYPE_ETF	=	'1'
#ETF基金
JG_TDC_STOCKTYPE_Option	=	'2'

#期权状态
#正常
JG_TDC_OPTIONSTATUS_Normal		  =    '0'
#临时停牌
JG_TDC_OPTIONSTATUS_Suspended	  =    '1'
#长期停牌
JG_TDC_OPTIONSTATUS_LongSuspended =	   '2'

#期权模式
#欧式
JG_TDC_OPTIONMODE_European	=	'0'
#美式
JG_TDC_OPTIONMODE_American	=	'1'

#开仓标识
#未开仓
JG_TDC_OPENTYPE_No	=	'0'
#开仓
JG_TDC_OPENTYPE_Yes	=	'1'

#停牌标识
#未停牌
JG_TDC_SUSPENDEDTYPE_No	 =	'0'
#停牌
JG_TDC_SUSPENDEDTYPE_Yes =	'1'


#到期日标识
#非到期日
JG_TDC_EXPIRETYPE_No	=	'0'
#到期日
JG_TDC_EXPIRETYPE_Yes	=	'1'


#调整标识
#未调整
JG_TDC_ADJUSTTYPE_No	=	'0'
#调整
JG_TDC_ADJUSTTYPE_Yes	=	'1'
