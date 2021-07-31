from django.http import HttpResponse
import sqlite3
from datetime import datetime, timedelta
import time 
import json

nameDb = 'db.sqlite3'
# デバッグの時はこっち
# nameDb = '../../db.sqlite3'
nameTable_withdrawal = 'MKsystemApp_withdrawal'
dict_withdrawalcolumn = {
    1: "id",
    2: "user_id",
    3: "date",
    4: "value",
    5: "status",
    6: "status_date",
    7: "operate_user_id",
}
nameTable_asset = 'MKsystemApp_asset'
dict_assetcolumn = {
    1: "id",
    2: "asset",
    3: "asset_date",
    4: "is_accept",
    5: "accept_date",
    6: "user_id",
}

nameTable_user = 'MKsystemApp_user'
dict_usercolumn = {
    1: "password",
    2: "last_login",
    3: "is_superuser",
    4: "user_id",
    5: "family_name",
    6: "first_name",
    7: "zip",
    8: "address",
    9: "phone",
    10: "date_joined",
    11: "is_staff",
    12: "is_active",
    13: "btc_address",
    14: "rank",
    15: "asset",
}
nameTable_deposit = 'MKsystemApp_deposit'
dict_depositcolumn = {
    1: "user_id",
    2: "deposit_value",
    3: "deposit_date",
    4: "operate_user_id",
}

nameTable_exchange = 'MKsystemApp_exchange'
dict_exchangecolumn = {
    1: "id",
    2: "rate",
    3: "date",
}


# if __name__ == '__main__':
#     conn = sqlite3.connect(nameDb)
#     cur = conn.cursor()
#     strSql = 'SELECT ' + dict_usercolumn[15] + \
#              ' FROM ' + nameTable_user + \
#              ' WHERE ' + dict_usercolumn[4] + '=?'
#     cur.execute(strSql, ("admin",))
#     asset_value = cur.fetchone()[0]
#     cur.close()
#     conn.close()


def change_status(id, str_status, operate_user_id):
    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()
    strSql = "UPDATE " + \
             nameTable_withdrawal + \
             " SET " + \
             dict_withdrawalcolumn[5] + "=?" + \
             ", " + dict_withdrawalcolumn[6] + "=?" + \
             ", " + dict_withdrawalcolumn[7] + "=?" + \
             " WHERE " + \
             dict_withdrawalcolumn[1] + "=" + id
    params = [(str_status, datetime.now() - timedelta(hours=9), operate_user_id)]
    cur.executemany(strSql, params)
    conn.commit()
    cur.close()
    conn.close()

    return HttpResponse(str_status)


def change_deposit(user_id, deposit_value, operate_user_id):
    # 一旦SELECTして足し算してUPDATEするか
    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()
    # strSql = 'SELECT ' + dict_usercolumn[15] + \
    #          ' FROM ' + nameTable_user + \
    #          ' WHERE ' + dict_usercolumn[4] + '=?'
    strSql = 'SELECT ' + dict_assetcolumn[2] + \
             ' FROM ' + nameTable_asset + \
             ' WHERE ' + dict_assetcolumn[6] + '=?'
    cur.execute(strSql, (user_id,))
    asset_value = float(cur.fetchone()[0])
    # 足し算してUPDATE
    update_value = asset_value + deposit_value
    # strSql = "UPDATE " + \
    #          nameTable_user + \
    #          " SET " + \
    #          dict_usercolumn[15] + "=?" + \
    #          " WHERE " + \
    #          dict_usercolumn[4] + "=?"
    strSql = "UPDATE " + \
             nameTable_asset + \
             " SET " + \
             dict_assetcolumn[2] + "=?, " + \
             dict_assetcolumn[3] + "=?" + \
             " WHERE " + \
             dict_assetcolumn[6] + "=?"
    params = [(update_value, datetime.now() - timedelta(hours=9), user_id)]
    cur.executemany(strSql, params)
    conn.commit()

    # depositテーブルに格納する
    strSql = 'INSERT INTO ' + nameTable_deposit + ' (' + \
             dict_depositcolumn[1] + ', ' + \
             dict_depositcolumn[2] + ', ' + \
             dict_depositcolumn[3] + ', ' + \
             dict_depositcolumn[4] + ') ' + \
             'VALUES (?,?,?,?)'
    params = (user_id, deposit_value, datetime.now() - timedelta(hours=9), operate_user_id)
    cur.execute(strSql, params)
    conn.commit()

    cur.close()
    conn.close()
    
    # time.sleep(1)
    
    return HttpResponse(update_value)


def read_exchange():
    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()

    # depositテーブルに格納する
    strSql = 'SELECT *'\
             ' FROM ' + nameTable_exchange
    cur.execute(strSql)
    data = cur.fetchone()

    cur.close()
    conn.close()
    
    return HttpResponse(json.dumps(data))
