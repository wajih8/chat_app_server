import sqlite3 as sql

"""
def rowcount(rows):
    t = []
    i = 0
    for row in rows:
        t.append(row)
        i += 1
    return i, t


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


def fetch_row(rows):
    t = ()
    for row in rows:
        t = row
    return t


ch = "wajih"

with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()
    res = cu.execute(
        f"select id,unid,name from users where name='{ch}' ")

    a = fetch_row(res)
    print(a)
