from django.core.management.base import BaseCommand
import json
import ccxt
import time
import subprocess
from MKsystemApp.management.commands.function import print_log
from MKsystemApp.management.commands.operatedatabase import *


# その日のBOTの資産状況をデータベースに入れる
class Command(BaseCommand):
    def handle(self, *args, **options):
        # if __name__ == '__main__':
        name_file = "run001"

        try:
            str_log = "[run001]Start"
            print_log(str_log, name_file)
            # まず時刻合わせする
            proc = subprocess.Popen("net start w32time", shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            ret = proc.communicate()[0].decode('cp932')
            str_log = "[run001]net start w32time:{}".format(ret)
            print_log(str_log, name_file)
            time.sleep(1)
            proc = subprocess.Popen("w32tm /resync", shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)  # DEVNULL
            ret = proc.communicate()[0].decode('cp932')
            str_log = "[run001]w32tm /resync:{}".format(ret)
            print_log(str_log, name_file)

            # ポジション持ってもtotalは変わらない
            # そのためtotalだけをデータベースに格納すればよい

            # BOTごとに取得する
            str_log = "[run001] BOT No.1"
            print_log(str_log, name_file)
            bykeyjson = open("apikey_bot1.json", "r")
            bykey = json.load(bykeyjson)
            ccxt_bybit = ccxt.bybit(bykey)

            balance = ccxt_bybit.fetch_balance()
            asset = float(balance['BTC']['total'])
            str_date = datetime.today()
            insert_botassets("1", asset, str_date)

            str_log = "[run001] BOT No.2"
            print_log(str_log, name_file)
            bykeyjson = open("apikey_bot2.json", "r")
            bykey = json.load(bykeyjson)
            ccxt_bybit = ccxt.bybit(bykey)

            balance = ccxt_bybit.fetch_balance()
            asset = float(balance['BTC']['total'])
            str_date = datetime.today()
            insert_botassets("2", asset, str_date)

            str_log = "[run001]Finish"
            print_log(str_log, name_file)

        except Exception as e:
            print_log(str(e), name_file)
            input()
