from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql
from func import *


xa = loads(sys.argv[1])

id1 = int(xa["iduser"])
id2 = int(xa["idfien"])
valid = xa["validation"]
with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()

    res = cu.execute(
        f"select value from coockie where id={id1} order by dateassi desc limit 1")
    e = {"wa": "<err1>your tocken is invalid"}
    x = fetch_row(res)

    if x == valid:
        e = {"wa": "<err2>you are not a frined with this user"}

        res = cu.execute(
            f"select idChat from friends where idFF={id1} and idSF={id2}")
        y = fetch_row(res)
        if y:
            e = {"wa": "<err3>ther is no massages beween you"}
            res = cu.execute(
                f"select idsender,message,dates from messages where (idsender={id1} or idsender={id2}) and idChat={y} order by dates limit 500")
            t = []
            for mes in fetch_rows(res):
                t.append({"idsender": mes[0], "idchat": y,
                         "message": mes[1], "date": mes[2]})
            if t != []:
                e["wa"] = t


print(dumps(e))
stdout.flush()
