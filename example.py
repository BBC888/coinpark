
#!-*-coding:utf-8 -*-
#@TIME    : 2018/6/25/0025 15:37
#@Author  : Nogo
#@File    : example.py

import REST.REST_API as CONST
from REST.REST_API import REST_API

api = REST_API()

key = ''
secret = ''
api = REST_API()
api.auth(key, secret)


r = api.get_kline('BIX_BTC','1min',100)
print(r)

#下单命令
cm1 = api.create_order_cmd(1, 'BIX_BTC', CONST.SIDE_BUY, 100000, 0.002, CONST.TYPE_LIMIT_PRICE, 0.002)
cm2 = api.create_order_cmd(2, 'BIX_BTC', CONST.SIDE_SELL, 100000, 0.002, CONST.TYPE_LIMIT_PRICE, 0.002)
r = api.multi_sign_cmd([cm1, cm2])
print(r)
