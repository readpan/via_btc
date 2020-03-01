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
    # text = '{"code":0,"data":{"account":{"account":"songyuan","country":null,"country_code":null,"create_time":1523768417,"email":null,"id":206913,"mobile":null,"parent_user_id":95456},"balance":[{"amount":"0.27466177","coin":"BTC"},{"amount":"0.32656496","coin":"ELA"},{"amount":"0.09201619","coin":"EMC"},{"amount":"1.3937384","coin":"NMC"},{"amount":"4.0000776","coin":"SYS"}],"observer":[],"withdraw_address":[{"address":"16R6kY3TKqwyc2oWm8qKXcAQj5psQkDioz","coin":"BTC"}]},"message":"OK"}'
    j = json.loads(r)['data']
    out = ''
    out += '当前账号余额：' + str(j['balance'][0]['amount']) + '\n'
    return out

def get_account_wallet():
    headers = {'X-API-KEY': 'ed91396c2c558a299ed41ea719a75ba0'}
    r = requests.get('https://www.viabtc.com/res/openapi/v1/account', headers=headers)
    # text = '{"code":0,"data":{"active_workers":3,"coin":"BTC","hashrate_10min":"44625511932668","hashrate_1hour":"41468691881365","hashrate_24hour":"41780627402430","unactive_workers":0},"message":"OK"}'
    j = json.loads(r)['data']
    out = ''
    out += '活跃机器：'+str(j["active_workers"])+'\n'
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
