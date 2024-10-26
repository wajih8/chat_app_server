
from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql


def rows(x):
    i = 0
    j = ""
    for j in x:
        i += 1
    return i, j


xa = loads(sys.argv[1])


da = xa["date"]
idse = int(xa["idse"])
idcha = int(xa["idch"])
mess = xa["mess"]
"""
da = "2024-07-04 05:48:41"
idse = 157
idcha = 1
mess = "wasa"
"""
# e = {"a": idse, "b": idcha, "c": mess, "d": da, "j": "ti bara rawah"}
with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()
    res = cu.execute(
        f"select * from messages where idsender={idse} and idChat={idcha} and message='{mess}' and dates='{da}'")
    i, t = rows(res)
    e = {"wa": "true"}
    if i > 0:

        res = cu.execute(
            f"select * from messages where idChat={idcha} order by dates desc limit 1")
        i, t = rows(res)

        if t[0] == idse and t[1] == idcha and t[2] == mess and da == t[3]:
            e = {"wa": "false"}


print(dumps(e))
stdout.flush()
