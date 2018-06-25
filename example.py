
#!-*-coding:utf-8 -*-
#@TIME    : 2018/6/25/0025 15:37
#@Author  : Nogo
#@File    : example.py

from REST.REST_API import REST_API

api = REST_API()

key = ''
secret = ''
api = REST_API()
api.auth(key, secret)


r = api.get_kline('BIX_BTC','1min',100)
print(r)

#下单命令
cm1 = api.create_order_cmd(1, 'BIX_BTC', 1, 2, 0.002, 1, 0.002)
cm2 = api.create_order_cmd(2, 'BIX_BTC', 1, 2, 0.002, 1, 0.002)
r = api.multi_sign_cmd([cm1, cm2])
print(r)
