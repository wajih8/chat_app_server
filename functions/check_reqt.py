
from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql
from func import fetch_rows, fetch_row2


def clean(t):
    t1 = []
    for i in t:
        t1.append(i[0])
    return t1


xa = loads(sys.argv[1])


da = int(xa["ids"])

with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()
    res = cu.execute(
        f"select idFF from friends where accept='false' and idSF='{da}'")
    t = fetch_rows(res)

    e = {"wa": "true"}
    if t:
        t = clean(t)
        for j in t:
            res = cu.execute(
                f"select name,unid from users where id={j}")
            t2 = fetch_row2(res)
            e[t2[1]] = {"name": t2[0], "id": j}

print(dumps(e))
stdout.flush()
