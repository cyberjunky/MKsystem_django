import pandas as pd
import sqlite3
from datetime import datetime, timedelta

# バッチの時はこっち
nameDb = 'db.sqlite3'
# デバッグの時はこっち
nameDb = '../../../db.sqlite3'
nameTable_botassets = 'MKsystemApp_botassets'
dict_botassetscolumn = {1: "bot_no",
                        2: "asset",
                        3: "date"
                        }
nameTable_user_assets = 'MKsystemApp_user_assets'
dict_userassetscolumn = {1: "user_id",
                         2: "asset",
                         3: "date"
                         }
nameTable_asset = 'MKsystemApp_asset'
dict_assetcolumn = {1: "id",
                    2: "asset",
                    3: "asset_date",
                    4: "is_accept",
                    5: "accept_date",
                    6: "user_id",
                    7: "stop_date",
                    }

nameTable_exchange = 'MKsystemApp_exchange'
dict_exchangecolumn = {
    1: "id",
    2: "rate",
    3: "date",
}


def read_botassets(bot_no):
    datetimenow = datetime.now()
    datetimetarg = datetime(datetimenow.year,
                            datetimenow.month,
                            datetimenow.day)
    datetimetarg = datetimetarg - timedelta(days=7)

    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()
    strSql = "SELECT *" + \
             " FROM " + nameTable_botassets + \
             " WHERE " + dict_botassetscolumn[1] + "=? AND " + \
             dict_botassetscolumn[3] + ">=?"
    cur.execute(strSql, (bot_no, datetimetarg))
    data = cur.fetchall()
    cur.close()
    conn.close()
    print(data)

    # dataframeに変換
    df_botassets = pd.DataFrame(data)
    df_botassets[2] = pd.to_datetime(df_botassets[2])
    df_botassets[2] = df_botassets[2].map(lambda x: x.strftime("%Y-%m-%d"))
    print(df_botassets)


def insert_botassets(bot_no, asset, strdate):
    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()
    strSql = "INSERT INTO " + \
             nameTable_botassets + " (" + \
             dict_botassetscolumn[1] + \
             ", " + dict_botassetscolumn[2] + \
             ", " + dict_botassetscolumn[3] + \
             ") VALUES (?,?,?);"
    params = [(bot_no, asset, strdate)]
    cur.executemany(strSql, params)
    conn.commit()
    cur.close()
    conn.close()


def select_asset():
    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()
    strSql = "SELECT " + \
             dict_assetcolumn[6] + ", " + \
             dict_assetcolumn[2] + ", " + \
             dict_assetcolumn[4] + \
             " FROM " + nameTable_asset
    cur.execute(strSql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def insert_userassets(userassets):
    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()
    strSql = "INSERT INTO " + \
             nameTable_user_assets + " (" + \
             dict_userassetscolumn[1] + \
             ", " + dict_userassetscolumn[2] + \
             ", " + dict_userassetscolumn[3] + \
             ") VALUES (?,?,?);"
    cur.executemany(strSql, userassets)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    bot_no = "1"
    datetimenow = datetime.now()
    datetimetarg = datetime(datetimenow.year,
                            datetimenow.month,
                            datetimenow.day)
    datetimetarg = datetimetarg - timedelta(days=7)

    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()
    strSql = "SELECT *" + \
             " FROM " + nameTable_botassets + \
             " WHERE " + dict_botassetscolumn[1] + "=? AND " + \
             dict_botassetscolumn[3] + ">=?"
    cur.execute(strSql, (bot_no, datetimetarg))
    data = cur.fetchall()
    cur.close()
    conn.close()
    print(data)

    # dataframeに変換
    df_botassets = pd.DataFrame(data)
    df_botassets[2] = pd.to_datetime(df_botassets[2])
    df_botassets[2] = df_botassets[2].map(lambda x: x.strftime("%Y-%m-%d"))
    print(df_botassets)


def insert_exchange(rate):
    conn = sqlite3.connect(nameDb)
    cur = conn.cursor()

    # exchangeテーブルに格納する
    strSql = 'INSERT INTO ' + nameTable_exchange + ' (' + \
             dict_exchangecolumn[2] + ', ' + \
             dict_exchangecolumn[3] + ') ' + \
             'VALUES (?,?)'
    params = (rate, datetime.now() - timedelta(hours=9))
    cur.execute(strSql, params)
    conn.commit()

    cur.close()
    conn.close()
