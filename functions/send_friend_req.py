from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql
from func import *


def clean(t):
    t1 = []
    for i in t:
        t1.append(i[0])
    return t1


xa = loads(sys.argv[1])

ch = int(xa["idFF"])
ch2 = int(xa["idSF"])
ch3 = xa["username"]
e = dict()
e["wa"] = ""
with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()

    res = cu.execute(
        f"select accept from friends where idFF={ch} and idSF={ch2} ")

    t = fetch_rows(res)
    t = clean(t)
    try:
        if t[0] == "true":
            print(dumps({"error": "user already a friend"}))
            stdout.flush()
            exit(1)
        elif t[0] == "false":
            print(dumps({"error": "friend requset already sent"}))
            stdout.flush()
            exit(1)
    except:
        pass
    res = cu.execute(
        f"select idChat from friends where idFF={ch} order by idChat DESC limit 1 ")
    t2 = fetch_rows(res)
    t2 = clean(t2)
    i = int(t2[0])+1
    ass = cu.execute(
        f"INSERT INTO friends VALUES({i},{ch},{ch2},'false')")
    if ass:
        e = {"wa": "true"}
print(dumps(e))
stdout.flush()
