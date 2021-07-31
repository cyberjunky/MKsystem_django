from django.http import HttpResponse
import json
from datetime import datetime
from datetime import timedelta
import random
import sqlite3


nameDb = 'db.sqlite3'

nameTable_userassets = 'MKsystemApp_user_assets'
dict_userassetscolumn = {
    1: "user_id",
    2: "asset",
    3: "date",
}

# if __name__ == '__main__':
def get_profitdata():
    dict_data = {}
    dict_data["date"] = ["4/25"]
    dict_data["profit"] = ["100"]

    # dict_data["date"] = []
    # dict_data["profit"] = ['90.79', '100.09', '107.48', '104.43', '121.33', 
    #                        '114.24', '102.28', '119.45', '105.52', '117.36', 
    #                        '116.63', '99.65', '95.63', '117.47']
    # nowdate = datetime.now()
    # for i in range(13, -1, -1):
    #     dict_data["date"].append((nowdate - timedelta(days=i)).strftime("%m/%d"))
    #     dict_data["profit"].append("{:.2f}".format(random.uniform(90, 130)))

    json_data = json.dumps(dict_data)

    return HttpResponse(json_data)


def get_assetdata(user_id, asset):
    dict_data = {}
    nowdate = datetime.now() - timedelta(days=0)
    print((nowdate - timedelta(days=0)).strftime("%m/%d"))
    # リストにしないとエラーになる
    dict_data["date"] = []
    dict_data["asset"] = []
    
    # データベースから取ってくる
    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()
    strSql = "SELECT " + \
             dict_userassetscolumn[2] + \
             ", " + dict_userassetscolumn[3] + \
             " FROM " + nameTable_userassets + \
             " WHERE " + dict_userassetscolumn[1] + "=?"
    cur.execute(strSql, (user_id,))
    list_data = cur.fetchall()
    cur.close()
    conn.close()
    
    # データ加工
    for data in list_data:
        data_datetime = datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
        dict_data["date"].append(data_datetime.strftime("%m/%d"))
        dict_data["asset"].append(data[0])
        
    dict_data["date"].append(nowdate.strftime("%m/%d"))
    dict_data["asset"].append(asset)

    json_data = json.dumps(dict_data)

    return HttpResponse(json_data)
