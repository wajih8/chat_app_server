from pickle import load, dump
import sqlite3 as sql


def rowcount(rows):
    t = []
    i = 0
    for row in rows:
        t.append(row)
        i += 1
    return i, t


def verifcation_exist(a):
    tes = "error file load"
    with open(a, "rb")as f:
        try:

            e = load(f)
            ids = e["id"]
            uids = e["unid"]
            tes = "error data base open"
            with sql.connect("database/appdb.db")as db:
                cu = db.cursor()
                res = cu.execute(
                    f"select * from users where id={ids} and unid='{uids}' ")
                i, t = rowcount(res)
                tes = "error no user"

                if i == 1:

                    if t[0][0] == int(ids) and uids == t[0][1] and e["username"].upper() == t[0][2].upper():
                        tes = "user is valid"
        except:
            pass
    return tes


def user_exist(a, b):
    tes = False
    with sql.connect("database/appdb.db")as db:
        cu = db.cursor()

        res = cu.execute(
            f"select name,password from users where name='{a}' and password='{b}' ")
        i, t = rowcount(res)

        if i == 1:
            if b == t[0][1] and a.upper() == t[0][0].upper():
                tes = True
    return tes
