# coding:utf-8
"""python调用今古交易服务Dll库demo示例文件, Python3.6.1"""

# 引入今古交易api库
from api_hait_ehfz.jgtrade_api import *
from datetime import datetime

# 定义接收数据回调函数
g_clientID = ''

def OnRecvData(service_id, funcid, pdata, ndata, pRspInfo, nrequestid):
    ANSINFO = cast(pRspInfo, POINTER(JGtdcRspInfoField))
    print("*************funcid")
    print(TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Login.value)
    if funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Login.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            Ans = cast(pdata, POINTER(JGtdcRspUserLogin))
            print("[应答 Link %d]登录成功 客户号 %s" % (service_id, Ans.contents.szClientID.decode("gb2312", errors='ignore')))
            global g_clientID
            g_clientID = Ans.contents.szClientID.decode("gb2312", errors='ignore')
        else:
            print("[应答 Link %d]登录失败， Error： %s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Entrust.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcRspOrderInsert)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcRspOrderInsert))
                print("[应答 Link %d]下单应答成功  代码：%s, 市场：%d, 买卖方向：%d, 价格：%d,数量：%d, 合同号：%s"
                      % (service_id, Ans.contents.szStockCode.decode("gb2312", errors = 'ignore'),Ans.contents.nExchangeType, Ans.contents.nTradeType, Ans.contents.iEntrustPrice,
                         Ans.contents.iEntrustAmount, Ans.contents.szEntrustNo.decode("gb2312", errors = 'ignore')))
                i = i + 1
        else:
            print("[应答 Link %d]下单失败， Error： %s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryBusByPos.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_position = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_BusBypos.csv"
            )
            with open(fpath_position, 'a') as f:
                i = 0
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryTrade)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryTrade))
                    print("[应答 Link %d]成交查询成功 代码：%s, 市场：%d, 买卖方向：%d, 价格：%d,数量：%d,  合同号：%s"% (
                        service_id,
                        Ans.contents.szStockCode.decode("gb2312", errors='ignore'),
                        Ans.contents.nExchangeType,
                        Ans.contents.nTradeType,
                        Ans.contents.iEntrustPrice,
                        Ans.contents.iEntrustAmount,
                        Ans.contents.szEntrustNo.decode("gb2312", errors = 'ignore')))
                    list_values_cacct_position = [
                        str(x) for x in [
                            Ans.contents.szFundAccount.decode("gb2312", errors='ignore'),
                            Ans.contents.szStockCode.decode("gb2312", errors='ignore'),
                            Ans.contents.nExchangeType,
                            Ans.contents.nTradeType,
                            Ans.contents.iEntrustPrice,
                            Ans.contents.iEntrustAmount,
                            Ans.contents.szEntrustNo.decode("gb2312", errors='ignore')
                        ]
                    ]
                    str_dataline_csv_position = ','.join(list_values_cacct_position)
                    f.write(str_dataline_csv_position + '\n')
                    i = i + 1
            print("成交查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]成交查询失败， Error： %s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryEntrust.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcRspQryOrder)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcRspQryOrder))
                print("[应答 Link %d]委托查询成功 代码：%s, 市场：%d, 买卖方向：%d, 价格：%d,数量：%d, 合同号：%s"
                      % (service_id, Ans.contents.szStockCode.decode("gb2312", errors='ignore'), Ans.contents.nExchangeType, Ans.contents.nTradeType, Ans.contents.iEntrustPrice, Ans.contents.iEntrustAmount,
                      Ans.contents.szEntrustNo.decode("gb2312", errors = 'ignore')))
                i = i + 1
            print("委托查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]委托查询失败， Error： %s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryRevocEnt.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcRspQryCancel)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcRspQryCancel))
                print("[应答 Link %d]可撤单查询成功 代码：%s, 市场：%d, 买卖方向：%d, 价格：%d,数量：%d, 合同号：%s"
                      % (service_id, Ans.contents.szStockCode.decode("gb2312", errors='ignore'), Ans.contents.nExchangeType, Ans.contents.nTradeType, Ans.contents.iEntrustPrice, Ans.contents.iEntrustAmount,
                         Ans.contents.szEntrustNo.decode("gb2312", errors = 'ignore')))
                i = i + 1
            print("可撤单查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]可撤单查询失败， Error： %s" % ( service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryHold.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_position = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_position.csv"
            )
            with open(fpath_position, 'w') as f:
                i = 0
                list_keys_position = [
                    '资金账号', '代码', '市场', '昨日持仓量', '股份余额', '可卖数量', '可申购数量', '当前拥股数量', '成本价格', '证券市值',
                    '浮动盈亏'
                ]
                f.write(','.join(list_keys_position) + '\n')
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryHold)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryHold))
                    print(
                        "[应答 Link %d]持仓查询成功 代码：%s, 市场：%d, 昨日持仓量：%d, 股份余额：%d, 可卖数量: %d, "
                        "可申购数量: %d, 当前拥股数量: %d, 成本价格: %d, 证券市值: %2.f, 浮动盈亏: %2.f" % (
                            service_id,
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
                        )
                    )
                    list_values_cacct_position = [
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
                    str_dataline_csv_position = ','.join(list_values_cacct_position)
                    f.write(str_dataline_csv_position + '\n')
                    i = i + 1
                print("持仓查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]持仓查询失败， Error： %s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryShortsell.value:  # todo to check
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            list_keys_security_loan_contract = [
                '营业部号', '客户号', '资金账号', '市场类型', '股东代码', '席位号', '证券代码', '证券名称', '合同号', '@币种',
                '@负债现状', '发生日期', '发生数量', '发生金额', '归还数量', '归还金额'
            ]
            fpath_security_loan_contract = (
                f"D:/data/trddata/hait_ehfz_api/{datetime.today().strftime('%Y%m%d')}_security_loan_contract.csv"
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
                    list_dataline_security_loan_contract = [str(x) for x in list_values_security_loan_contract]
                    f.write(','.join(list_dataline_security_loan_contract) + '\n')
                    i = i + 1
                print("负债合约查询个数： %d" % ANSINFO.contents.nFieldItem)  # 发生数量: %d, 发生金额: %2.f, 发生日期：%d,
        else:
            print("[应答 Link %d]持仓查询失败， Error： %s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryFund.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_cacct_fund = f"D:/data/trddata/hait_ehfz_api/{datetime.today().strftime('%Y%m%d')}_cash_account_fund.csv"
            with open(fpath_cacct_fund, 'w') as f:
                i = 0
                list_keys_cacct_fund = ['资金账户', '币种', '可用余额', '可取余额', '冻结金额', '证券市值', '资金余额', '资产总值', '总盈亏']
                f.write(','.join(list_keys_cacct_fund) + '\n')
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryFund)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryFund))
                    print("[应答 Link %d]资金查询成功 币种：%s, 可用余额：%.2f, 可取余额：%.2f, 冻结金额：%.2f, 证券市值：%.2f, 资金余额：%.2f, 资产总值：%.2f, 总盈亏：%.2f "
                          % (service_id, Ans.contents.cMoneyType.decode("gb2312", errors='ignore'), Ans.contents.dEnableBalance, Ans.contents.dFetchBalance,
                             Ans.contents.dFrozenBalance, Ans.contents.dStockBalance, Ans.contents.dFundBalance, Ans.contents.dAssetBalance, Ans.contents.dInCome))
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
            print("[应答 Link %d]资金查询失败， Error： %s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryAssets.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            fpath_cacct_fund = (
                f"D:/data/trddata/investment_manager_products/hait_ehfz_api/"
                f"{datetime.today().strftime('%Y%m%d')}_credit_asset.csv"
            )
            with open(fpath_cacct_fund, 'w') as f:
                i = 0
                list_keys_cacct_fund = ['资金账号', '币种', '可用余额', '可取余额', '冻结金额', '证券市值', '资金余额', '资产总值', '总盈亏']
                f.write(','.join(list_keys_cacct_fund) + '\n')
                while i < ANSINFO.contents.nFieldItem:
                    offset = i * sizeof(JGtdcRspQryFund)
                    pTmpData = pdata + offset
                    Ans = cast(pTmpData, POINTER(JGtdcRspQryFund))
                    print("[应答 Link %d]资金查询成功 币种：%s, 可用余额：%.2f, 可取余额：%.2f, 冻结金额：%.2f, 证券市值：%.2f, 资金余额：%.2f, 资产总值：%.2f, 总盈亏：%.2f "
                          % (service_id, Ans.contents.cMoneyType.decode("gb2312", errors='ignore'), Ans.contents.dEnableBalance, Ans.contents.dFetchBalance,
                             Ans.contents.dFrozenBalance, Ans.contents.dStockBalance, Ans.contents.dFundBalance, Ans.contents.dAssetBalance, Ans.contents.dInCome))
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
            print("[应答 Link %d]资金查询失败， Error： %s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Cancel.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            Ans = cast(pdata, POINTER(JGtdcRspOrderCancel))
            print("[应答 Link %d]撤单成功, 合同号：%s" % (g_serviceid, Ans.contents.szEntrustNo.decode("gb2312", errors = 'ignore')) )
        else:
            print("[应答 Link %d]撤单失败， Error：%s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryMax.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            Ans = cast(pdata, POINTER(JGtdcRspQryMax))
            print("[应答 Link %d]最大交易数量查询成功, 最大数量：%d" % (g_serviceid, Ans.contents.iMaxAmount) )
        else:
            print("[应答 Link %d]最大交易数量查询失败， Error：%s" % (service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
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

def Login(account, password, g_serviceid):
    login = JGtdcReqUserLogin()
    login.cLoginType = bytes(JG_TDC_LOGINTYPE_FundAccount, encoding="gb2312")
    login.szLoginCode = bytes(account, encoding="gb2312")
    login.szLoginPassword = bytes(password, encoding="gb2312")
    login.szMACAddress = bytes("00163E1A38A5", encoding="gb2312")
    login.szIPAddress = bytes("192.168.1.248", encoding="gb2312")
    login.szMD5 = bytes("", encoding="gb2312")
    temp = cast(pointer(login), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Login.value, temp, 1, 0)):
        print("发送登录成功")
    else:
        print("发送登录失败")

def QryEntrust(g_serviceid):
    req = JGtdcReqQryOrder()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryEntrust.value, temp, 1, 0)):
        print("查询委托成功")
    else:
        print("查询委托失败")

def QryBusiness(g_serviceid):
    req = JGtdcReqQryTrade()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryBusByPos, temp, 1, 0)):
        print("查询成交成功")
    else:
        print("查询成交失败")

def QryHold(g_serviceid):
    req = JGtdcReqQryHold()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryHold.value, temp, 1, 0)):
        print("查询持仓成功")
    else:
        print("查询持仓失败")

def QryFund(g_serviceid):
    req = JGtdcReqQryFund()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryAssets.value, temp, 1, 0)):
        print("查询资金成功")
    else:
        print("查询资金失败")

def QryShortsell(g_serviceid):
    req = JGtdcReqQryHold()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryShortsell.value, temp, 1, 0)):
        print("查询融券状况成功")
    else:
        print("查询融券状况失败")


# 创建回掉函数对象
_jgtradeapi_notice_cb_ = OnTradeLinkCallBack(OnNoticeData)
_jgtradeapi_data_cb_ = OnTradeDataCallBack(OnRecvData)


# 主函数
if __name__ == "__main__":
    API_Start()
    # 创建服务
    # global g_serviceid
    # 此处传参：账户类型； serviceid: Bool 表示创建service是否成功，与 service type 不一样
    g_serviceid = API_CreateService(TRADETYPE.TD_STOCK.value)  # 账户类型调整
    # 注册回调
    register_Linkcallback(g_serviceid, _jgtradeapi_notice_cb_)
    register_Datacallback(g_serviceid, _jgtradeapi_data_cb_)

    # 连接服务器
    API_Connect(g_serviceid, c_char_p(b"124.74.252.82"), 8980, False)  # 此处传参： 交易服务器参数

    print("请输入数字使用正确指令：[0]登录, [1]下单, [2]撤单, [3]可撤单查询, [4]委托查询, [5]成交查询, [6]持仓查询, [7]资金查询, [8]最大交易数量查询, [9]退出")
    while 1:
        n = input()
        if int(n) == 0:
            Login("0920111727", "123321", TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Login, g_serviceid)
            print(gl.g_clientID)
        elif int(n) == 1:
            print("下单")
            Entrust()
        elif int(n) == 2:
            print("撤单")
            Cancel()
        elif int(n) == 3:
            print("可撤单查询")
            QryCancel()
        elif int(n) == 4:
            print("委托查询")
            QryEntrust()
        elif int(n) == 5:
            print("成交查询")
            QryBusiness(TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryBusByPos, g_clientID)
        elif int(n) == 6:
            print("持仓查询")
            QryHold()
        elif int(n) == 7:
            print("资金查询")
            QryFund()
        elif int(n) == 8:
            print("最大交易数量查询")
            QryMax()
        elif int(n) == 9:
            print("退出")
            break
        elif int(n) == 10:
            print("融券负债情况查询")
            QryShortsell()
        elif int(n) == 11:
            Login("0790888666", "123321", TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Login, g_serviceid)
        else:
            print("未知指令,请重新输入：[1]下单, [2]撤单, [3]可撤单查询, [4]委托查询, [5]成交查询, [6]持仓查询, [7]资金查询, [8]最大交易数量查询, [9]退出")

    if g_serviceid > 0:
        API_DisConnect(g_serviceid)
        API_Stop()
        print("end")
