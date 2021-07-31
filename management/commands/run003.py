from django.core.management.base import BaseCommand
from MKsystemApp.management.commands.function import print_log
from MKsystemApp.management.commands.operatedatabase import *
import requests


# その日のBOTの資産状況をデータベースに入れる
# class Command(BaseCommand):
#     def handle(self, *args, **options):
if __name__ == '__main__':
    name_file = "run003"

    try:
        str_log = "[run003]Start"
        print_log(str_log, name_file)

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

        str_log = "[run003]last_ticker:{}".format(last_ticker)
        print_log(str_log, name_file)

        # user_assetに書き込む
        insert_exchange(last_ticker)

        str_log = "[run003]Finish"
        print_log(str_log, name_file)

    except Exception as e:
        print_log(str(e), name_file)
        input()
