import sqlite3 as sql
from json import load
import datetime
from socket import *
"""
def rowcount(rows):
    t = []
    i = 0
    for row in rows:
        t.append(row)
        i += 1
    return i, t

da = str(datetime.datetime.now())[:10]
with sql.connect("database/appdb.db")as db:
    cu = db.cursor()

    res = cu.execute(
        f"select  from users where name='wajih' and password='wajih3' ")
    i, t = rowcount(res)

    print(t, i)

import datetime
z = datetime.datetime.day
print(z)
daa = datetime.datetime.date(datetime.datetime.now())
datetime.timedelta.total_seconds(datetime.datetime.now())
"""
"""

def fetch_row(rows):
    t = ()
    for row in rows:
        t = row
    return t


with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()
    with open("messages.json", "r")as f:
        data = load(f)
    data = data["e1248a142"]
    for da in data:
        idsch = da["idchat"]
        idsender = da["idsender"]
        mess = da["message"]
        dat = da["date"]
        res = cu.execute(
            f"INSERT into messages VALUES ({idsender},{idsch},'{mess}','{dat}')")
        print("wa")

print(gethostbyname(gethostname()))
"""
with open("tests/temp.dat", "rb")as f:
    print(load(f))
