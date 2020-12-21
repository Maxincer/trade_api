# coding:utf-8
"""python调用今古交易服务Dll库demo示例文件, Python3.6.1"""

# 引入今古交易api库
from api_hait_ehfz.jgtrade_api import *
from datetime import datetime

g_clientID = ''


# 定义接收数据回调函数
def OnRecvData(service_id, funcid, pdata, ndata, pRspInfo, nrequestid):
    global g_clientID
    ANSINFO = cast(pRspInfo, POINTER(JGtdcRspInfoField))

    # 登录返回
    if funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Login.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            Ans = cast(pdata, POINTER(JGtdcRspUserLogin))
            g_clientID = Ans.contents.szClientID.decode("gb2312", errors='ignore')
        else:
            print(
                "[应答 Link %d]登录失败， Error： %s"
                % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore'))
            )
    # 普通户
    # 查询普通户资金
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryFund.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_cacct_fund = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_{g_clientID}_cash_account_fund.csv"
            )
            with open(fpath_cacct_fund, 'w') as f:
                i = 0
                list_keys_cacct_fund = ['资金账户', '币种', '可用余额', '可取余额', '冻结金额', '证券市值', '资金余额', '资产总值', '总盈亏']
                f.write(','.join(list_keys_cacct_fund) + '\n')
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryFund)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryFund))
                    list_values_cacct_fund = [
                        str(x) for x in
                        [Ans.contents.szFundAccount.decode("gb2312", errors='ignore'),
                         Ans.contents.cMoneyType.decode("gb2312", errors='ignore'),
                         Ans.contents.dEnableBalance,
                         Ans.contents.dFetchBalance,
                         Ans.contents.dFrozenBalance,
                         Ans.contents.dStockBalance,
                         Ans.contents.dFundBalance,
                         Ans.contents.dAssetBalance,
                         Ans.contents.dInCome]
                    ]
                    f.write(','.join(list_values_cacct_fund) + '\n')
                    i = i + 1
            print("资金查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print(
                "[应答 Link %d]资金查询失败， Error： %s"
                % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore'))
            )

    # 查询普通户持仓
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryHold.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_holding = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_{g_clientID}_cash_account_holding.csv"
            )
            with open(fpath_holding, 'w') as f:
                i = 0
                list_keys_holding = [
                    '资金账号', '代码', '市场', '昨日持仓量', '股份余额', '可卖数量',
                    '可申购数量', '当前拥股数量', '成本价格', '证券市值', '浮动盈亏'
                ]
                f.write(','.join(list_keys_holding) + '\n')
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryHold)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryHold))
                    list_values_cacct_holding = [
                        str(x) for x in [
                            Ans.contents.szFundAccount.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockCode.decode("gb2312", errors='ignore'),
                            Ans.contents.nExchangeType,
                            Ans.contents.iYdAmount,
                            Ans.contents.iStockAmount,
                            Ans.contents.iEnableAmount,
                            Ans.contents.iPurchaseAmount,
                            Ans.contents.iPossessAmount,
                            Ans.contents.iKeepCostPrice,
                            Ans.contents.dStockBalance,
                            Ans.contents.dFloatIncome
                        ]
                    ]
                    str_dataline_csv_holding = ','.join(list_values_cacct_holding)
                    f.write(str_dataline_csv_holding + '\n')
                    i = i + 1
                print("持仓查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]持仓查询失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))

    # 查询普通户成交
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryBusByPos.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_busbypos = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_{g_clientID}_cash_account_trade.csv"
            )
            with open(fpath_busbypos, 'w') as f:
                list_fields_cacct_busbypos = [
                    '客户号', '资金账号', '市场类型', '股东代码', '席位号', '证券代码', '证券名称', '定位串', '合同号',
                    '成交编号', '@币种', '@成交状态', '@交易类型', '@价格类型', '成交日期', '成交时间', '委托数量', '委托价格',
                    '成交数量', '成交价格', '撤销数量', '成交金额'
                ]
                str_fields_cacct_busbypos = ','.join(list_fields_cacct_busbypos) + '\n'
                f.write(str_fields_cacct_busbypos)

            with open(fpath_busbypos, 'a') as f:
                i = 0
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryTrade)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryTrade))
                    list_values_cacct_busbypos = [
                        str(x) for x in [
                            Ans.contents.szBranchNo.decode('gbk', errors='ignore'),
                            Ans.contents.szClientID.decode('gbk', errors='ignore'),
                            Ans.contents.szFundAccount.decode("gb2312", errors='ignore'),
                            Ans.contents.nExchangeType,
                            Ans.contents.szStockAccount.decode("gb2312", errors='ignore'),
                            Ans.contents.szSeatNo.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockCode.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockName.decode("gb2312", errors='ignore'),
                            Ans.contents.szPositionStr.decode("gb2312", errors='ignore'),
                            Ans.contents.szEntrustNo.decode("gb2312", errors='ignore'),
                            Ans.contents.szBusinessNo.decode("gb2312", errors='ignore'),
                            Ans.contents.cMoneyType.decode("gb2312", errors='ignore'),
                            Ans.contents.cBusinessStatus.decode("gb2312", errors='ignore'),
                            Ans.contents.nTradeType,
                            Ans.contents.nPriceType,
                            Ans.contents.nBusinessDate,
                            Ans.contents.nBusinessTime,
                            Ans.contents.iEntrustAmount,
                            Ans.contents.iEntrustPrice,
                            Ans.contents.iEntrustAmount,
                            Ans.contents.iEntrustPrice,
                            Ans.contents.iBusinessAmount,
                            Ans.contents.iBusinessPrice,
                            Ans.contents.iCancelAmount,
                            Ans.contents.dBusinessBalance,
                        ]
                    ]
                    str_dataline_csv_busbypos = ','.join(list_values_cacct_busbypos)
                    f.write(str_dataline_csv_busbypos + '\n')
                    i = i + 1
            print("成交查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print(
                "[应答 Link %d]成交查询失败， Error： %s"
                % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore'))
            )

    # 信用户
    # 查询信用户资金
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryAssets.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_macct_fund = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_{g_clientID}_margin_account_fund.csv"
            )
            with open(fpath_macct_fund, 'w') as f:
                i = 0
                list_keys_macct_fund = [
                    '营业部号', '客户号', '资金帐号', '@币种', '可用余额', '可取余额', '冻结金额', '证券市值', '资金余额', '资产总值',
                    '总盈亏', '可用保证金', '授信额度', '可融资金', '可融券额度', '维持担保比例', '总负债', '资金负债', '股票负债',
                    '应还金额'
                ]
                f.write(','.join(list_keys_macct_fund) + '\n')
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryAssets)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryAssets))
                    list_values_macct_fund = [
                        str(x) for x in [
                            Ans.contents.szBranchNo.decode("gb2312", errors='ignore'),
                            Ans.contents.szClientID.decode("gb2312", errors='ignore'),
                            Ans.contents.szFundAccount,
                            Ans.contents.cMoneyType,
                            Ans.contents.dEnableBalance,
                            Ans.contents.dFetchBalance,
                            Ans.contents.dFrozenBalance,
                            Ans.contents.dStockBalance,
                            Ans.contents.dFundBalance,
                            Ans.contents.dAssetBalance,
                            Ans.contents.dIncome,
                            Ans.contents.dEnableBail,
                            Ans.contents.dCreditQuota,
                            Ans.contents.dFinanceQuota,
                            Ans.contents.dShortsellQuota,
                            Ans.contents.dAssureRatio,
                            Ans.contents.dTotalDebit,
                            Ans.contents.dFundDebit,
                            Ans.contents.dStockDebit,
                            Ans.contents.dMustBackBalance,
                        ]
                    ]
                    f.write(','.join(list_values_macct_fund) + '\n')
                    i = i + 1
            print("资金查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print(
                "[应答 Link %d]资金查询失败， Error： %s"
                % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore'))
            )

    # 信用户持仓
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryHold.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_holding = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_{g_clientID}_margin_account_holding.csv"
            )
            with open(fpath_holding, 'w') as f:
                i = 0
                list_keys_holding = [
                    '营业部号', '客户号', '资金账号', '股东代码', '证券代码', '证券名称', '市场类型', '@币种', '昨日持仓量', '股份余额',
                    '可卖数量', '可申购数量', '当前拥股数量', '冻结数量', '昨日库存数量', '成本价格', '保本价格', '当前成本', '证券市值',
                    '浮动盈亏', '累计盈亏'
                ]
                f.write(','.join(list_keys_holding) + '\n')
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryHold)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryHold))
                    list_values_cacct_holding = [
                        str(x) for x in [
                            Ans.contents.szBranchNo.decode("gb2312", errors='ignore'),
                            Ans.contents.szClientID.decode("gb2312", errors='ignore'),
                            Ans.contents.szFundAccount.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockAccount.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockCode.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockName.decode("gb2312", errors='ignore'),
                            Ans.contents.nExchangeType,
                            Ans.contents.cMoneyType,
                            Ans.contents.iYdAmount,
                            Ans.contents.iStockAmount,
                            Ans.contents.iEnableAmount,
                            Ans.contents.iPurchaseAmount,
                            Ans.contents.iPossessAmount,
                            Ans.contents.iFrozenAmount,
                            Ans.contents.iYStoreAmount,
                            Ans.contents.iCostPrice,
                            Ans.contents.iKeepCostPrice,
                            Ans.contents.dBuyCost,
                            Ans.contents.dStockBalance,
                            Ans.contents.dFloatIncome,
                            Ans.contents.dProIncome
                        ]
                    ]
                    str_dataline_csv_holding = ','.join(list_values_cacct_holding)
                    f.write(str_dataline_csv_holding + '\n')
                    i = i + 1
                print("持仓查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print(
                "[应答 Link %d]持仓查询失败， Error： %s"
                % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore'))
            )

    # 信用户成交
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryBusByPos.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_busbypos = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_{g_clientID}_margin_account_trade.csv"
            )
            with open(fpath_busbypos, 'w') as f:
                list_fields_macct_busbypos = [
                    '营业部号', '客户号', '资金账号', '市场类型', '股东代码', '席位号', '证券代码', '证券名称', '定位串', '合同号',
                    '成交编号', '@币种', '@成交状态', '@交易类型', '@价格类型', '成交日期', '成交时间', '委托数量', '委托价格',
                    '成交数量', '成交价格', '撤销数量', '成交金额'
                ]
                str_fields_macct_busbypos = ','.join(list_fields_macct_busbypos) + '\n'
                f.write(str_fields_macct_busbypos)

            with open(fpath_busbypos, 'a') as f:
                i = 0
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryTrade)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryTrade))
                    list_values_macct_busbypos = [
                        str(x) for x in [
                            Ans.contents.szBranchNo.decode('gbk', errors='ignore'),
                            Ans.contents.szClientID.decode('gbk', errors='ignore'),
                            Ans.contents.szFundAccount.decode("gb2312", errors='ignore'),
                            Ans.contents.nExchangeType,
                            Ans.contents.szStockAccount.decode("gb2312", errors='ignore'),
                            Ans.contents.szSeatNo.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockCode.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockName.decode("gb2312", errors='ignore'),
                            Ans.contents.szPositionStr.decode("gb2312", errors='ignore'),
                            Ans.contents.szEntrustNo.decode("gb2312", errors='ignore'),
                            Ans.contents.szBusinessNo.decode("gb2312", errors='ignore'),
                            Ans.contents.cMoneyType.decode("gb2312", errors='ignore'),
                            Ans.contents.cBusinessStatus.decode("gb2312", errors='ignore'),
                            Ans.contents.nTradeType,
                            Ans.contents.nPriceType,
                            Ans.contents.nBusinessDate,
                            Ans.contents.nBusinessTime,
                            Ans.contents.iEntrustAmount,
                            Ans.contents.iEntrustPrice,
                            Ans.contents.iBusinessAmount,
                            Ans.contents.iBusinessPrice,
                            Ans.contents.iCancelAmount,
                            Ans.contents.dBusinessBalance,
                        ]
                    ]
                    str_dataline_csv_busbypos = ','.join(list_values_macct_busbypos)
                    f.write(str_dataline_csv_busbypos + '\n')
                    i = i + 1
            print("成交查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print(
                "[应答 Link %d]成交查询失败， Error： %s"
                % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore'))
            )

    # 信用户: 融券状况
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryShortsell.value:  # todo to check
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            list_keys_security_loan_contract = [
                '营业部号', '客户号', '资金账号', '市场类型', '股东代码', '席位号', '证券代码', '证券名称', '合同号', '@币种',
                '@负债现状', '发生日期', '发生数量', '发生金额', '归还数量', '归还金额',
            ]
            fpath_security_loan_contract = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api"
                f"/{datetime.today().strftime('%Y%m%d')}_{g_clientID}_margin_account_security_loan.csv"
            )
            with open(fpath_security_loan_contract, 'w') as f:
                f.write(','.join(list_keys_security_loan_contract) + '\n')
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryShortsell)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryShortsell))
                    list_values_security_loan_contract = [
                        Ans.contents.szBranchNo.decode("gb2312", errors='ignore'),
                        Ans.contents.szClientID.decode("gb2312", errors='ignore'),
                        Ans.contents.szFundAccount.decode("gb2312", errors='ignore'),
                        Ans.contents.nExchangeType,
                        Ans.contents.szStockAccount.decode("gb2312", errors='ignore'),
                        Ans.contents.szSeatNo.decode("gb2312", errors='ignore'),
                        Ans.contents.szStockCode.decode("gb2312", errors='ignore'),
                        Ans.contents.szStockName.decode("gb2312", errors='ignore'),
                        Ans.contents.szEntrustNo.decode("gb2312", errors='ignore'),
                        Ans.contents.cMoneyType.decode("gb2312", errors='ignore'),
                        Ans.contents.cDebitStatus.decode("gb2312", errors='ignore'),
                        Ans.contents.nOccurDate,
                        Ans.contents.iOccurAmount,
                        Ans.contents.dOccurBalance,
                        Ans.contents.iBackAmount,
                        Ans.contents.dBackBalance,
                    ]
                    list_dataline_security_loan = [str(x) for x in list_values_security_loan_contract]
                    f.write(','.join(list_dataline_security_loan) + '\n')
                    i = i + 1
                print("负债合约查询个数： %d" % ANSINFO.contents.nFieldItem)  # 发生数量: %d, 发生金额: %2.f, 发生日期：%d,
        else:
            print(
                "[应答 Link %d]持仓查询失败， Error： %s"
                % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore'))
            )

    else:
        print("未知的数据回调...")


# 定义通知消息回调函数
def OnNoticeData(service_id, linktype, errorinfo):
    if linktype == LINK_NOTICE_TYPE.LINK_NOTICE_TYPE_CONNECTE_SUCCESSED.value:
        print("成功连接交易服务器，[link %d]" % service_id)
    elif linktype == LINK_NOTICE_TYPE.LINK_NOTICE_TYPE_DISCONNECTED.value:
        print("断开交易服务器，link[%d] %s" % (service_id, errorinfo.decode('gbk')))
    else:
        print("未知的通知...")


def log_in(account, password, __g_serviceid):
    login = JGtdcReqUserLogin()
    login.cLoginType = bytes(JG_TDC_LOGINTYPE_FundAccount, encoding="gb2312")
    login.szLoginCode = bytes(account, encoding="gb2312")
    login.szLoginPassword = bytes(password, encoding="gb2312")
    login.szMACAddress = bytes("00163E1A38A5", encoding="gb2312")
    login.szIPAddress = bytes("192.168.1.248", encoding="gb2312")
    login.szMD5 = bytes("", encoding="gb2312")
    temp = cast(pointer(login), c_char_p)
    if 0 == API_TradeSend(__g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Login.value, temp, 1, 0):
        print("发送登录成功")
    else:
        print("发送登录失败")


def query_cacct_fund(__g_serviceid):
    req = JGtdcReqQryFund()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    temp = cast(pointer(req), c_char_p)
    if 0 == API_TradeSend(__g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryFund.value, temp, 1, 0):
        print("查询资金成功")
    else:
        print("查询资金失败")


def query_cacct_holding(__g_serviceid):
    req = JGtdcReqQryHold()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if 0 == API_TradeSend(__g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryHold.value, temp, 1, 0):
        print("查询持仓成功")
    else:
        print("查询持仓失败")


def query_cacct_trade(__g_serviceid):
    req = JGtdcReqQryTrade()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if 0 == API_TradeSend(__g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryBusByPos.value, temp, 1, 0):
        print("查询成交成功")
    else:
        print("查询成交失败")


def query_macct_fund(__g_serviceid):
    req = JGtdcReqQryAssets()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    temp = cast(pointer(req), c_char_p)
    if 0 == API_TradeSend(__g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryFund.value, temp, 1, 0):
        print("查询资金成功")
    else:
        print("查询资金失败")


def query_macct_holding(__g_serviceid):
    req = JGtdcReqQryHold()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if 0 == API_TradeSend(__g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryHold.value, temp, 1, 0):
        print("查询持仓成功")
    else:
        print("查询持仓失败")


def query_macct_trade(__g_serviceid):
    req = JGtdcReqQryTrade()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if 0 == API_TradeSend(__g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryBusByPos.value, temp, 1, 0):
        print("查询成交成功")
    else:
        print("查询成交失败")


def query_short_sell(__g_serviceid):
    req = JGtdcReqQryHold()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if 0 == API_TradeSend(__g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryShortsell.value, temp, 1, 0):
        print("查询融券状况成功")
    else:
        print("查询融券状况失败")
