# app.py
# -*- coding: UTF-8 -*-
from flask import Flask
from pip._vendor import requests
import json
import time

app = Flask(__name__)



def get_account_hashrate():
    # api without signature, send request with X-API-KEY header
    args = {'coin': 'BTC'}
    headers = {'X-API-KEY': 'ed91396c2c558a299ed41ea719a75ba0'}
    r = requests.get('https://pool.viabtc.com/res/openapi/v1/hashrate', params=args, headers=headers)
    j = json.loads(r.text)
    out = ''
    out += '当前账号余额：' + j["balance"][0]['amount'] + '\n'
    return out

def get_account_wallet():
    headers = {'X-API-KEY': 'ed91396c2c558a299ed41ea719a75ba0'}
    r = requests.get('https://www.viabtc.com/res/openapi/v1/account', headers=headers)
    j = json.loads(r.text)
    out = ''
    out += '活跃机器：'+j["active_workers"]+'\n'
    out += '一小时算力：'+str(float(j["hashrate_1hour"])/1000000000000)+'\n'
    return out

@app.route("/")
def hello():
    responses = ''
    responses += get_account_hashrate()
    responses += get_account_wallet()
    to_send_msg = 'https://sc.ftqq.com/SCU61940T3553c7eb29d0115392096e47a7f60fd35e54a4c36cd76.send?text='+time.asctime(time.localtime(time.time()))+'&desp='+responses
    requests.get(to_send_msg)
    return responses

if __name__ == "__main__":
    app.run(host='0.0.0.0')
