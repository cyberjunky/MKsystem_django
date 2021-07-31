from django.core.management.base import BaseCommand
import json
import ccxt
import time
import subprocess
from datetime import datetime, timedelta
from MKsystemApp.management.commands.function import print_log
from MKsystemApp.management.commands.operatedatabase import *


# その日のBOTの資産状況をデータベースに入れる
class Command(BaseCommand):
    def handle(self, *args, **options):
# if __name__ == '__main__':
        name_file = "run002"
    
        try:
            str_log = "[run002]Start"
            print_log(str_log, name_file)
    
            # assetテーブルから資産を取得する
            str_log = "[run002] select_asset"
            print_log(str_log, name_file)
            assets = select_asset()
            str_log = "[run002] assets:\n"
            for asset in assets:
                str_log += "{},{},{}\n".format(asset[0], asset[1], asset[2])
            print_log(str_log, name_file)
            
            # データ加工
            userassets = []
            now = datetime.now()
            asset_date = datetime(now.year, now.month, now.day)
            asset_date = asset_date - timedelta(days=1)
            for asset in assets:
                if not asset[2]:
                    continue
                userassets.append((asset[0], asset[1], asset_date))
            
            # user_assetに書き込む
            insert_userassets(userassets)
    
            str_log = "[run002]Finish"
            print_log(str_log, name_file)
    
        except Exception as e:
            print_log(str(e), name_file)
            input()
