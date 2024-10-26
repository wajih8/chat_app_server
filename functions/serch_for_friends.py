from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql


def fetch_rows(rows):
    t = []
    for row in rows:
        t.append(row)
    return t


def clean(t):
    t1 = []
    for i in t:
        t1.append(i[0])
    return t1


xa = loads(sys.argv[1])

ch =  xa["id"]

with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()
    
    res = cu.execute(
        f"select idSF from friends where idFF={ch} and accept='true';")
    t = clean(fetch_rows(res))
    res2 = cu.execute(
        f"select idFF from friends where idSF={ch} and accept='true';")
    t2 = clean(fetch_rows(res2))

    if t == [] and t2 == []:
        print(dumps({"error": "no user found"}))
        exit(1)
    e = dict()
    aba = []

    for i in t:

        sa = dict()
        res = cu.execute(
            f"select id,unid,name from users where id={i} ")
        frie = fetch_rows(res)

        sa["id"], sa["unid"], sa["name"] = frie[0][0], frie[0][1], frie[0][2]

        aba.append(sa)
    for i in t2:

        sa = dict()
        res = cu.execute(
            f"select id,unid,name from users where id={i} ")
        frie = fetch_rows(res)

        sa["id"], sa["unid"], sa["name"] = frie[0][0], frie[0][1], frie[0][2]

        aba.append(sa)
    e["friends"] = aba
    with open("tes.txt", "w")as f:
        f.write(dumps(e))
print(dumps(e))
stdout.flush()
