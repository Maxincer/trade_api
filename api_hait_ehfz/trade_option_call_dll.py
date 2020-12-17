# coding:utf-8
"""python调用今古交易服务Dll库demo示例文件, Python3.6.1"""

# 引入今古交易api库
from jgtrade_api import *


# 定义接收数据回调函数
def OnRecvData(service_id, funcid, pdata, ndata, pRspInfo, nrequestid):
    ANSINFO = cast(pRspInfo, POINTER(JGtdcRspInfoField))
    if funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_Login.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            Ans = cast(pdata, POINTER(JGtdcRspUserLogin))
            print(
                "[应答 Link %d]登录成功 客户号 %s" % (service_id, Ans.contents.szClientID.decode("gb2312", errors='ignore')))
            global g_clientID
            g_clientID = Ans.contents.szClientID.decode("gb2312", errors='ignore')
        else:
            print("[应答 Link %d]登录失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_Entrust.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcOptionRspEntrust)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcOptionRspEntrust))
                print("[应答 Link %d]下单应答成功 编码：%s 市场：%d 买卖方向：%d 价格：%d 数量：%d 合同号：%s"
                      % (service_id, Ans.contents.szContractNumber.decode("gb2312", errors='ignore'),
                         Ans.contents.nExchangeType, Ans.contents.nTradeType, Ans.contents.iEntrustPrice,
                         Ans.contents.iEntrustAmount,
                         Ans.contents.szEntrustNo.decode("gb2312", errors='ignore')))
                i = i + 1
        else:
            print("[应答 Link %d]下单失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_Cancel.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            Ans = cast(pdata, POINTER(JGtdcOptionRspCancel))
            print("[应答 Link %d]撤单成功, 合同号：%s " % (
            g_serviceid, Ans.contents.szEntrustNo.decode("gb2312", errors='ignore')))
        else:
            print("[应答 Link %d]撤单失败， Error：%s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryContract.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcOptionRspQryContract)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryContract))
                print("[应答 Link %d]合约查询成功 合约代码：%s 合约编码：%s 证券名称：%s 币种：%s 期权状态：%s 到期日标识：%s 调整标识：%s"
                      % (service_id, Ans.contents.szContractCode.decode("gb2312", errors='ignore'),
                         Ans.contents.szContractNumber.decode("gb2312", errors='ignore'),
                         Ans.contents.szStockName.decode("gb2312", errors='ignore'),
                         Ans.contents.cMoneyType.decode("gb2312", errors='ignore'),
                         Ans.contents.cOptionStatus.decode("gb2312", errors='ignore'),
                         Ans.contents.cExpireType.decode("gb2312", errors='ignore'),
                         Ans.contents.cAdjustType.decode("gb2312", errors='ignore')))
                i = i + 1
            print("合约查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]合约查询失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryEntrust.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcOptionRspQryEntrust)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryEntrust))
                print("[应答 Link %d]委托查询成功 编码：%s, 市场：%d, 买卖方向：%d, 价格：%d,数量：%d, 合同号：%s, 成交金额：%d"
                      % (service_id, Ans.contents.szContractNumber.decode("gb2312", errors='ignore'),
                         Ans.contents.nExchangeType, Ans.contents.nTradeType, Ans.contents.iEntrustPrice,
                         Ans.contents.iEntrustAmount,
                         Ans.contents.szEntrustNo.decode("gb2312", errors='ignore'), Ans.contents.dBusinessBalance))
                i = i + 1
            print("委托查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]委托查询失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryRevocEnt.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcOptionRspQryRevocEnt)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryRevocEnt))
                print("[应答 Link %d]可撤单查询成功 编码：%s, 市场：%d 委托数量：%d 成交金额：%d 撤销数量：%d"
                      % (service_id, Ans.contents.szContractNumber.decode("gb2312", errors='ignore'),
                         Ans.contents.nExchangeType, Ans.contents.iEntrustAmount, Ans.contents.dBusinessBalance,
                         Ans.contents.iCancelAmount))
                i = i + 1
            print("可撤单查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]可撤单查询失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryFund.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcOptionRspQryFund)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryFund))
                print(
                    "[应答 Link %d]资金查询成功 币种：%s, 可用余额：%.2f, 可取余额：%.2f, 冻结金额：%.2f, 证券市值：%.2f, 资金余额：%.2f, 资产总值：%.2f, 总盈亏：%.2f , 可用保证金：%.2f, 已用保证金：%.2f, 履约担保比例：%.2f, 风险度：%.2f, 风险度1：%.2f"
                    % (service_id, Ans.contents.cMoneyType.decode("gb2312", errors='ignore'),
                       Ans.contents.dEnableBalance, Ans.contents.dFetchBalance,
                       Ans.contents.dFrozenBalance, Ans.contents.dStockBalance, Ans.contents.dFundBalance,
                       Ans.contents.dAssetBalance, Ans.contents.dInCome, Ans.contents.dEnableBail,
                       Ans.contents.dUsedBail, Ans.contents.dAgreeAssureRatio, Ans.contents.dRiskRatio,
                       Ans.contents.dRiskRatio1))
                i = i + 1
            print("资金查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]资金查询失败， Error： %s" % (
                service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryHold.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcOptionRspQryHold)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryHold))
                print("[应答 Link %d]持仓查询成功 客户号：%s 合约编码：%s 持仓盈亏：%.2f 平仓盈亏：%.2f"
                      % (service_id, Ans.contents.szClientID.decode("gb2312", errors='ignore'),
                         Ans.contents.szContractNumber.decode("gb2312", errors='ignore'),
                         Ans.contents.dHoldIncome, Ans.contents.dPayoffIncome))
                i = i + 1
            print("持仓查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]持仓查询失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryBusByPos.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcOptionRspQryBusByPos)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryBusByPos))
                print("[应答 Link %d]成交查询成功 编码：%s 市场：%d 买卖方向：%d 价格：%d 数量：%d 合同号：%s, 成交金额：%d"
                      % (service_id, Ans.contents.szContractNumber.decode("gb2312", errors='ignore'),
                         Ans.contents.nExchangeType, Ans.contents.nTradeType, Ans.contents.iEntrustPrice,
                         Ans.contents.iEntrustAmount,
                         Ans.contents.szEntrustNo.decode("gb2312", errors='ignore'), Ans.contents.dBusinessBalance))
                i = i + 1
            print("成交查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]成交查询失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryCoveredHold.value:
        if ANSINFO.contents.nResultType == JG_TDC_ANSRESULT_Success:
            i = 0
            while i < ANSINFO.contents.nFieldItem:
                offset = i * sizeof(JGtdcOptionRspQryCoveredHold)
                pTmpData = pdata + offset
                Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryCoveredHold))
                print("[应答 Link %d]持仓查询成功 客户号：%s 股东代码：%s 股份余额：%d 可卖数量：%d"
                      % (service_id, Ans.contents.szClientID.decode("gb2312", errors='ignore'),
                         Ans.contents.szStockAccount.decode("gb2312", errors='ignore'),
                         Ans.contents.iStockAmount, Ans.contents.iEnableAmount))
                i = i + 1
            print("持仓查询个数： %d" % ANSINFO.contents.nFieldItem)
        else:
            print("[应答 Link %d]持仓查询失败， Error： %s" % (
            service_id, ANSINFO.contents.szErrorInfo.decode("gb2312", errors='ignore')))
    else:
        print("未知的数据回调...")

# 定义接收推送数据回调函数
def OnRecvPushData(service_id,funcid, pdata, ndata):
    if funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryBusByPos.value:
        i = 0
        while i < ndata:
            offset = i * sizeof(JGtdcOptionRspQryBusByPos)
            pTmpData = pdata + offset
            Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryBusByPos))
            print("[应答 Link %d]推送成交数据 编码：%s 市场：%d 买卖方向：%d 价格：%d 数量：%d 合同号：%s, 成交金额：%d"
                  % (service_id, Ans.contents.szContractNumber.decode("gb2312", errors='ignore'),
                     Ans.contents.nExchangeType, Ans.contents.nTradeType, Ans.contents.iEntrustPrice,
                     Ans.contents.iEntrustAmount,
                     Ans.contents.szEntrustNo.decode("gb2312", errors='ignore'), Ans.contents.dBusinessBalance))
            i = i + 1
        print("推送成交成交查询个数： %d" % ndata)
    elif funcid == TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryEntrust.value:
        i = 0
        while i < ndata:
            offset = i * sizeof(JGtdcOptionRspQryEntrust)
            pTmpData = pdata + offset
            Ans = cast(pTmpData, POINTER(JGtdcOptionRspQryEntrust))
            print("[应答 Link %d]推送委托数据 编码：%s, 市场：%d, 买卖方向：%d, 价格：%d,数量：%d, 合同号：%s, 成交金额：%d"
                  % (service_id, Ans.contents.szContractNumber.decode("gb2312", errors='ignore'),
                     Ans.contents.nExchangeType, Ans.contents.nTradeType, Ans.contents.iEntrustPrice,
                     Ans.contents.iEntrustAmount,
                     Ans.contents.szEntrustNo.decode("gb2312", errors='ignore'), Ans.contents.dBusinessBalance))
            i = i + 1
        print("推送委托查询个数： %d" % ndata)

# 定义通知消息回调函数
def OnNoticeData(service_id, linktype, errorinfo):
    if linktype == LINK_NOTICE_TYPE.LINK_NOTICE_TYPE_CONNECTE_SUCCESSED.value:
        print("成功连接交易服务器，[link %d]" % service_id)
    elif linktype == LINK_NOTICE_TYPE.LINK_NOTICE_TYPE_DISCONNECTED.value:
        print("断开交易服务器，link[%d] %s" % (service_id, errorinfo))
    else:
        print("未知的通知...")


# 创建回掉函数对象
_jgtradeapi_notice_cb_ = OnTradeLinkCallBack(OnNoticeData)
_jgtradeapi_data_cb_ = OnTradeDataCallBack(OnRecvData)
_jgtradeapi_data_push_cb_ = OnTradePushDataCallBack(OnRecvPushData)


def Login():
    login = JGtdcReqUserLogin()

    login.cLoginType = bytes(JG_TDC_LOGINTYPE_FundAccount, encoding="gb2312")
    login.szLoginCode = bytes("9095000128", encoding="gb2312")
    login.szLoginPassword = bytes("147258", encoding="gb2312")
    login.szMACAddress = bytes("AAC5BAFDABCC", encoding="gb2312")
    login.szIPAddress = bytes("10.10.10.10", encoding="gb2312")
    temp = cast(pointer(login), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_Login.value, temp, 1, 0)):
        print("发送登录成功")
    else:
        print("发送登录失败")


def Entrust():
    # nItem = 2
    req = JGtdcOptionReqEntrust()

    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.szContractNumber = bytes("10002436", encoding="gb2312")
    req.nExchangeType = TJGtdcExchangeType.JG_TDC_EXCHANGETYPE_OPTSHA.value
    req.nTradeType = JG_TDC_TRADETYPE_Buy
    req.iEntrustPrice = 1900
    req.iEntrustAmount = 1
    req.nPriceType = JG_TDC_PRICETYPE_Limit
    req.cOffsetType = JG_TDC_OFFSETTYPE_Open
    req.cCoveredType = JG_TDC_COVEREDTYPE_No
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_Entrust.value, temp, 1, 0)):
        print("下单请求：编码：%s, 市场：%d, 买卖方向：%d, 价格：%d,数量：%d" %
              (req.szContractNumber.decode("gb2312", errors='ignore'), req.nExchangeType, req.nTradeType,
               req.iEntrustPrice, req.iEntrustAmount))
    else:
        print("下单失败")


def Cancel():
    req = JGtdcOptionReqCancel()
    print("请输入要撤单的合同号：")
    szEntrust = input()
    req.szEntrustNo = bytes(szEntrust, encoding="gb2312")
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nExchangeType = 2

    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_Cancel.value, temp, 1, 0)):
        print("发送撤单成功")
    else:
        print("发送撤单失败")


def QryContract():
    req = JGtdcOptionReqQryContract()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))

    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryContract.value, temp, 1, 0)):
        print("查询合约成功")
    else:
        print("查询合约失败")


def QryEntrust():
    req = JGtdcOptionReqQryEntrust()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))

    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryEntrust.value, temp, 1, 0)):
        print("查询委托成功")
    else:
        print("查询委托失败")


def QryCancel():
    req = JGtdcOptionReqQryRevocEnt()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))

    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryRevocEnt.value, temp, 1, 0)):
        print("查询可撤单成功")
    else:
        print("查询可撤单失败")


def QryBusiness():
    req = JGtdcOptionReqQryBusByPos()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryBusByPos.value, temp, 1, 0)):
        print("查询成交成功")
    else:
        print("查询成交失败")


def QryHold():
    req = JGtdcOptionReqQryHold()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    req.nQueryDirection = int(bytes(JG_TDC_QUERYDIRECTION_Inverted, encoding="gb2312"))
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryHold.value, temp, 1, 0)):
        print("查询持仓成功")
    else:
        print("查询持仓失败")


def QryFund():
    req = JGtdcOptionReqQryFund()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryFund.value, temp, 1, 0)):
        print("查询资金成功")
    else:
        print("查询资金失败")


def QryCoveredHold():
    req = JGtdcOptionReqQryCoveredHold()
    req.szClientID = bytes(g_clientID, encoding="gb2312")
    req.nQueryMode = TJGtdcQueryMode.JG_TDC_QUERYMODE_All.value
    temp = cast(pointer(req), c_char_p)
    if (0 == API_TradeSend(g_serviceid, TRADE_FUNCID_TYPE.JG_FUNCID_OPTION_QryCoveredHold.value, temp, 1, 0)):
        print("查询备兑持仓成功")
    else:
        print("查询备兑持仓失败")


# 主函数
if __name__ == "__main__":
    print("start")

    # 初始化服务
    API_Start()

    # 创建服务
    global g_serviceid
    g_serviceid = API_CreateService(TRADETYPE.TD_OPTION.value)
    # 注册回调
    register_Linkcallback(g_serviceid, _jgtradeapi_notice_cb_)
    register_Datacallback(g_serviceid, _jgtradeapi_data_cb_)
    register_PushDatacallback(g_serviceid,_jgtradeapi_data_push_cb_)

    # 连接服务器
    API_Connect(g_serviceid, c_char_p(b"180.166.179.196"), 5912, False)

print("请输入数字使用正确指令：[0]登录, [1]下单, [2]撤单 ,[3]合约查询, [4]委托查询, [5]可撤单查询, [6]成交查询, [7]持仓查询, [8]资金查询,[9]备兑持仓查询, [15]退出")
while 1:
    n = input()

    if int(n)   == 0:
        Login()
    elif int(n) == 1:
        print("下单")
        Entrust()
    elif int(n) == 2:
        print("撤单")
        Cancel()
    elif int(n) == 3:
        print("合约查询")
        QryContract()
    elif int(n) == 4:
        print("委托查询")
        QryEntrust()
    elif int(n) == 5:
        print("可撤单查询")
        QryCancel()
    elif int(n) == 6:
        print("成交查询")
        QryBusiness()
    elif int(n) == 7:
        print("持仓查询")
        QryHold()
    elif int(n) == 8:
        print("资金查询")
        QryFund()
    elif int(n) == 9:
        print("备兑持仓查询")
        QryCoveredHold()
    elif int(n) == 15:
        print("退出")
        break
    else :
        print("未知指令,请重新输入：[1]下单, [2]撤单, [3]合约查询, [4]委托查询, [5]可撤单查询, [6]成交查询, [7]持仓查询, [8]资金查询, [9]备兑持仓查询, [15]退出")



if g_serviceid > 0:
    API_DisConnect(g_serviceid)
    API_Stop()
    print("end")
