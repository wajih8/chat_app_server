from func import *
from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql
import datetime

xa = loads(sys.argv[1])
idu = xa["iduser"]
idf = xa["idfien"]
mess = xa["message"]
da = str(datetime.datetime.now())[:19]
with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()

    res = cu.execute(
        f"select idChat from friends where idFF={idu} and idSF={idf}")
    i = fetch_row(res)
    e = {"wa": "false"}
    if i:
        try:
            res = cu.execute(
                f"INSERT INTO messages values({idu},{i},'{mess}','{da}')")
            e = {"wa": "true"}
        except:
            pass


print(dumps(e))
stdout.flush()
