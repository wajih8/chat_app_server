from json import loads, dumps
import sqlite3 as sql
import datetime


def cryptage(uid, user):
    da = str(datetime.datetime.now())[:10]
    s = str(datetime.datetime.now())[11:19]
    s = s[:2]+s[3:5]+s[6:]

    x = ord("a")
    while len(user) < 10:
        user += chr(x)
        x += 1

    user2 = ""
    for i in range(len(user)):
        if da[i] == "-":
            user2 += user[i]+"k"
        else:
            user2 += user[i]+da[i]

    chcry = ""
    j = -1
    for i in range(len(user2)):
        if j == len(uid)-1:
            j = -1
        else:
            j += 1
        chcry += crypt(user2[i], uid[j])
    chcry = chcry[:4]+s[:2]+chcry[4:8]+s[2:4]+chcry[8:12]+s[4:]+chcry[12:]
    chcry
    return (chcry)


def crypt(a, b):
    x = ord(b) % 26
    if x+ord(a) > ord("9") and x+ord(a) < ord("A"):
        return chr(x+ord(a)-9)
    elif x+ord(a.upper()) > ord("Z"):
        return chr(x+ord(a)-26)
    else:
        return chr(x+ord(a))


def fetch_row(rows):

    for row in rows:
        t = row
    return t


def get_userinfo(a, b):
    with sql.connect("database/appdb.db")as db:
        cu = db.cursor()
        res = cu.execute(
            f"select id,unid,name from users where name='{a}' and password='{b}' ")
        t = fetch_row(res)

        e = dict()
        e['id'], e['uniqueid'], e['username'] = t[0], t[1], t[2]
        ids = t[0]

        e["validation"] = cryptage(t[1], t[2])
        y = e["validation"]
        print(e["validation"], t[1], t[2])
        da = str(datetime.datetime.now())[:19]
        cu.execute(
            f"INSERT into 'coockie' values({ids},'{da}','{y}') ")
        x = dumps(e)
    return x
