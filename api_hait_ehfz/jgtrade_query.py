# coding:utf-8
import trade_stock_call_dll as tscd
from datetime import datetime
import pandas as pd
from jgtrade_api import *
import globalvar as gl

def get_acct_pwd(acct_psw_file_path):
    """
    读取acct_pwd文件中的product id，account number和password，并且判断该account是信用户还是普通户
    :param acct_psw_file_path: 记录账号密码的文件（csv），columns = [PrdCode: int64，AcctIDByMXZ: string，AcctIDByBroker: int64，Pwd: int64]
    :return acct_psw_dic: dictionary，{‘xy’：{‘proid’：[account_number, password]},‘pt’：{‘proid’：[account_number, password]}}
    """
    acct_psw_df = pd.read_excel(acct_psw_file_path, dtype = {'PrdCode': str, 'AcctIDByBroker': str, 'Pwd':str})
    acct_psw_df['AcctType'] = acct_psw_df['AcctIDByMXZ'].apply(lambda x: x.split('_')[1])
    xy_dict = {}
    pt_dict = {}
    for i in range(len(acct_psw_df)):
        proid = acct_psw_df.loc[i, 'PrdCode']
        account_number = acct_psw_df.loc[i, 'AcctIDByBroker']
        password = acct_psw_df.loc[i, 'Pwd']
        if acct_psw_df.loc[i, 'AcctType'] == 'c':
            pt_dict[proid] = [str(account_number), str(password)]
        elif acct_psw_df.loc[i, 'AcctType'] == 'm':
            xy_dict[proid] = [str(account_number), str(password)]
        else:
            print('acct_psw file有错，请检查！！')
            quit()
    acct_psw_dic = {'xy': xy_dict, 'pt': pt_dict}
    return acct_psw_dic


# 主函数
if __name__ == "__main__":

    # 读取资金账户和密码
    acct_psw_file_path = r'hait_acct_psw.xlsx'
    acct_psw_dic = get_acct_pwd(acct_psw_file_path)
    #账户类型
    tradetype = {'xy': TRADETYPE.TD_CREDIT.value, 'pt': TRADETYPE.TD_STOCK.value}
    # 股票生产地址
    address_port = {'xy': [b'124.74.252.82', 8930], 'pt': [b'124.74.252.82', 8901]}
    # TRADE_FUNCID_TYPE
    trade_funcid_type = {'xy':{'Login': TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_Login, 'Holding': TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryHold,
                               'Fund': TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryFund, 'Trading': TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryBusByPos,
                               'SecLoan': TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_QryShortsell, 'Logout': TRADE_FUNCID_TYPE.JG_FUNCID_CREDIT_Logout},
                         'pt':{'Login': TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Login, 'Holding': TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryHold,
                               'Fund': TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryFund, 'Trading': TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_QryBusByPos,
                               'Logout': TRADE_FUNCID_TYPE.JG_FUNCID_STOCK_Logout}}

    for k,v in acct_psw_dic.items():
        if len(v) != 0:

            for proid,acct_psw in v.items():
                # 获取账号
                account = acct_psw[0]
                password = acct_psw[1]

                if k == 'pt':
                    # 初始化服务
                    API_Start()
                    # 创建服务
                    # global g_serviceid
                    # 此处传参：账户类型； serviceid: Bool 表示创建service是否成功，与 service type 不一样
                    g_serviceid = API_CreateService(tradetype[k])  # 账户类型调整

                    # 注册回调
                    register_Linkcallback(g_serviceid, tscd._jgtradeapi_notice_cb_)
                    register_Datacallback(g_serviceid, tscd._jgtradeapi_data_cb_)

                    # 连接服务器
                    API_Connect(g_serviceid, c_char_p(address_port[k][0]), address_port[k][1], False)  # 此处传参： 交易服务器参数

                    # 普通户：登录，成交查询，持仓查询，资金查询，退出
                    # 1. 登录

                    tscd.Login(account, password, trade_funcid_type[k]['Login'], g_serviceid)
                    print(gl.g_clientID)
                    # 2. 成交查询
                    tscd.QryBusiness(trade_funcid_type[k]['Trading'], g_clientID)
                    # 3. 持仓查询
                    # QryHold(trade_funcid_type[k]['Holding'])
                    # 4. 资金
                    # QryFund(trade_funcid_type[k]['Fund'])

                else:
                    # 信用户：登录，成交查询，持仓查询，资金查询，融券状况查询，退出
                    # 1. 登录
                    Login(account, password, trade_funcid_type[k]['Login'])
                    # 2. 成交查询
                    QryBusiness(trade_funcid_type[k]['Trading'])
                    # 3. 持仓查询
                    QryFund(trade_funcid_type[k]['Holding'])
                    # 4. 融券状况查询
                    QryShortsell()
                    # 5. 退出



            #
            # trade_fpath_position = (f"C:/Users/Administrator/Desktop/test/trade_pt.csv")
            # with open(trade_fpath_position, 'w') as f:
            #     list_keys_position = ['资金账号', '代码', '市场', '买卖方向', '价格', '数量', '合同号']
            #     f.write(','.join(list_keys_position) + '\n')


            # holding_fpath_position = {f"D:/data/trddata/test/holding_pt.csv"}
            # with open(holding_fpath_position, 'a') as f:
            #     list_keys_position = ['资金账号', '代码', '市场', '买卖方向', '价格', '数量', '合同号']
            #     f.write(','.join(list_keys_position) + '\n')
            # fund_fpath_position = {f"D:/data/trddata/test/fund_pt.csv"}
            # with open(fund_fpath_position, 'a') as f:
            #     list_keys_position = ['资金账号', '代码', '市场', '买卖方向', '价格', '数量', '合同号']
            #     f.write(','.join(list_keys_position) + '\n')
            #
            #     trade_fpath_position = {f"D:/data/trddata/test/trade_pt.csv"}
            #     with open(trade_fpath_position, 'a') as f:
            #         list_keys_position = ['资金账号', '代码', '市场', '买卖方向', '价格', '数量', '合同号']
            #         f.write(','.join(list_keys_position) + '\n')
            #     holding_fpath_position = {f"D:/data/trddata/test/holding_pt.csv"}
            #     with open(holding_fpath_position, 'a') as f:
            #         list_keys_position = ['资金账号', '代码', '市场', '买卖方向', '价格', '数量', '合同号']
            #         f.write(','.join(list_keys_position) + '\n')
            #     fund_fpath_position = {f"D:/data/trddata/test/fund_pt.csv"}
            #     with open(fund_fpath_position, 'a') as f:
            #         list_keys_position = ['资金账号', '代码', '市场', '买卖方向', '价格', '数量', '合同号']
            #         f.write(','.join(list_keys_position) + '\n')


 # # trading csv
    # pt_trading = pd.DataFrame(columns=['资金账户', '代码', '市场', '买卖方向', '价格', '数量', '合同号'])
    # xy_trading = pd.DataFrame(columns=['资金账户', '代码', '市场', '买卖方向', '价格', '数量', '合同号'])
    # trade = {'xy': xy_trading, 'pt': pt_trading}
    #
    # # holding csv
    # pt_holding = pd.DataFrame(columns=['资金账户', '代码', '市场', '昨日持仓量', '股份余额', '可卖数量', '可申购数量', '当前拥股数量', '成本价格', '证券市值', '浮动盈亏'])
    # xy_holding = pd.DataFrame(columns=['资金账户', '代码', '市场', '昨日持仓量', '股份余额', '可卖数量', '可申购数量', '当前拥股数量', '成本价格', '证券市值', '浮动盈亏'])
    # holding = {'xy':xy_holding, 'pt': pt_holding}
    #
    # # fund csv
    # pt_fund = pd.DataFrame(columns=['资金账户', '币种', '可用余额', '可取余额', '冻结金额', '证券市值', '资金余额', '资产总值', '总盈亏'])
    # xy_fund = pd.DataFrame(columns=['资金账户', '币种', '可用余额', '可取余额', '冻结金额', '证券市值', '资金余额', '资产总值', '总盈亏'])
    # fund = {'xy': xy_fund, 'pt': pt_fund}
    #
    # # SecLoan csv
    # xy_SecLoan = pd.DataFrame(columns=['资金账户', '营业部号', '客户号', '市场类型', '股东代码', '席位号', '证券代码', '证券名称', '合同号', '@币种', '@负债现状', '发生日期', '发生数量', '发生金额', '归还数量', '归还金额'])
