# app.py
# -*- coding: UTF-8 -*-
from flask import Flask
from pip._vendor import requests

app = Flask(__name__)



def get_account_hashrate():
    # api without signature, send request with X-API-KEY header
    args = {'coin': 'BTC'}
    headers = {'X-API-KEY': 'ed91396c2c558a299ed41ea719a75ba0'}
    r = requests.get('https://pool.viabtc.com/res/openapi/v1/hashrate', params=args, headers=headers)
    return r.text

def get_account_wallet():
    headers = {'X-API-KEY': 'ed91396c2c558a299ed41ea719a75ba0'}
    r = requests.get('https://www.viabtc.com/res/openapi/v1/account', headers=headers)
    return r.text

@app.route("/")
def hello():
    responses = ''
    responses += get_account_hashrate()
    responses += '\n'
    responses += get_account_wallet()
    import time
    to_send_msg = 'https://sc.ftqq.com/SCU61940T3553c7eb29d0115392096e47a7f60fd35e54a4c36cd76.send?text='+time.asctime(time.localtime(time.time()))+'&desp='+responses
    requests.get(to_send_msg)
    return responses

if __name__ == "__main__":
    app.run(host='0.0.0.0')
