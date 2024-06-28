from sys import stdout
from json import dumps, loads
import sys
import sqlite3 as sql


def fetch_row(rows):
    t = ()
    for row in rows:
        t = row
    return t


xa = loads(sys.argv[1])
ch = xa["name"]

with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()
    res = cu.execute(
        f"select id,unid,name from users where name='{ch}' ")

    t = fetch_row(res)
    if t == ():
        print(dumps({"error": "no user found"}))
        exit(1)

    e = dict()
    e["id"], e["unid"], e["name"] = t[0], t[1], t[2]
    with open("tes.txt", "a")as f:
        f.write(e["unid"]+"|||||||||||"+e["name"])
print(dumps(e))
stdout.flush()
"""


ch = sys.argv[1]
# ch = "wajih"
with sql.connect("./database/appdb.db")as db:
    cu = db.cursor()
    res = cu.execute(
        f"select id,unid,name from users where name='{ch}' ")
    t = fetch_row(res)
    e = dict()
    e["id"], e["unid"], e["name"] = t[0], t[1], t[2]
print(dumps({"s": "ti bara zamer"}))
stdout.flush()
    """
