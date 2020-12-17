#globalvar.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

g_clientID = 'none'

def _init():
    global g_clientID
    g_clientID = 'none'
    # global _global_dict
    # _global_dict = {}
#
# def set_value(name, value):
#     _global_dict[name] = value
#
# def get_value(name, defValue = None):
#     try:
#         return _global_dict[name]
#     except:
#         return defValue