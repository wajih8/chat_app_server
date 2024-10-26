from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql



def fetch_rows(rows):
    t = []
    for row in rows:
        print(row)
        t.append(row)
    return t


def clean(t):
    t1 = []
    for i in t:
        t1.append(i[0])
    return t1


# xa = loads(sys.argv[1])

ch = "157"  # xa["id"])

with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()

    res = cu.execute('SELECT * FROM friends')
    res2 = cu.execute(
        f"select idFF from friends where idSF={ch} and accept='true' ")
    for i in res:
        print(i)
    # t = clean(fetch_rows(res))
    t2 = clean(fetch_rows(res2))
    print(t2)
