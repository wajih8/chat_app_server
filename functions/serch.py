from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql


def fetch_rows(rows):
    t = []
    for row in rows:
        try:
            e = {"id": row[0], "name": row[1], "unid": row[2], "tes": True}
            t.append(e)
        except:
            pass
    return t


def fetch_rows2(rows):
    t = []
    for row in rows:
        try:
            t.append(row[0])
        except:
            pass
    return t


xa = loads(sys.argv[1])

ch = xa["name"]
ids = int(xa["ids"])
"""ch = "wajih"
ids = 157"""

with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()

    res = cu.execute(
        f"select id,name,unid from users where name='{ch}' or name like '{ch}%'")
    t = fetch_rows(res)
    if t == []:
        print(dumps({"error": "no user found"}))
        exit(1)
    res = cu.execute(
        f"select idSF from friends where idFF={ids} ")
    t2 = fetch_rows2(res)
    for i in t2:
        for j in t:
            if j["id"] == i or j["id"] == ids:
                j["tes"] = False
    e = dict()
    e["Friend_tes"] = "good"
    aba = []
    for i in t:
        if i["tes"] == True:
            sa = dict()
            sa["id"], sa["unid"], sa["name"] = i["id"], i["unid"], i["name"]
            aba.append(sa)
    e["Friend_ava"] = aba
    if aba == []:
        e["Friend_tes"] = "ther is no user with this name"

    with open("tes.txt", "w")as f:
        f.write(dumps(e)+"\n")
        f.write(str(ids)+"   -   "+ch)
print(dumps(e))
stdout.flush()
