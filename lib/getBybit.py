from django.http import HttpResponse
import json
import ccxt
import requests
import time
import os
import subprocess


if __name__ == '__main__':
    dict_balance = {}
    bykeyjson = open("apikey_bot{}.json".format(2), "r")
    bykey = json.load(bykeyjson)
    ccxt_bybit = ccxt.bybit(bykey)
    balance = ccxt_bybit.fetch_balance()
    dict_balance["total_btc"] = balance['BTC']['total']
    dict_balance["free_btc"] = balance['BTC']['free']
    
    proc = subprocess.Popen("net start w32time", shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    ret = proc.communicate()[0].decode('cp932')
    print(ret)
    time.sleep(1)
    proc = subprocess.Popen("w32tm /resync", shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)  # DEVNULL
    ret = proc.communicate()[0].decode('cp932')
    print(ret)
    
def get_balance(bot_no):
    # まず時刻合わせする
    if bot_no == "1":
        proc = subprocess.Popen("net start w32time", shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        ret = proc.communicate()[0].decode('cp932')
        time.sleep(1)
        proc = subprocess.Popen("w32tm /resync", shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)  # DEVNULL
        ret = proc.communicate()[0].decode('cp932')

    # print(os.getcwd())
    # if __name__ == '__main__':
    dict_balance = {}
    bykeyjson = open("apikey_bot{}.json".format(bot_no), "r")
    bykey = json.load(bykeyjson)
    ccxt_bybit = ccxt.bybit(bykey)

    balance = ccxt_bybit.fetch_balance()
    dict_balance["total_btc"] = balance['BTC']['total']
    dict_balance["free_btc"] = balance['BTC']['free']

    return HttpResponse(json.dumps(dict_balance))
    # print(json.dumps(dict_balance))


def get_usdrate():
    # time.sleep(10)
    URL = "https://api.coingecko.com/api/v3"
    endpoint = "/coins/"
    coins = "bitcoin"
    url = URL + endpoint + coins
    req = requests.request("GET", url)
    str_json = req.json()

    last_ticker = 0
    list_tickers = str_json["tickers"]
    for ticker in list_tickers:
        if ticker["base"] == "BTC" and \
            ticker["target"] == "USD" and \
            ticker["market"]["name"] == "FTX.US":
            last_ticker = ticker["last"]
            break
    return HttpResponse(last_ticker)
