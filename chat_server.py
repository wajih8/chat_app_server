from socket import *
from tqdm import tqdm
import os
import threading
import time
from verifcation import verifcation_exist, user_exist
from functions import get_userinfo
server = socket(AF_INET, SOCK_STREAM)
addr = (gethostbyname(gethostname()), 6030)
server.bind(addr)
FORMAT = "utf-8"


def handel(conn, b):
    print("new user connected", b)
    sepa = ""
    while True:
        msghead = conn.recv(64).decode()

        if msghead:
            if msghead.find("!disco") != -1:
                break
            else:
                sepa = msghead[:msghead.find("|")]
                fullmsg = conn.recv(2048)
                user = str(b[0][:3])
                if sepa == "verlogin":
                    try:
                        os.mkdir(user)
                    except:
                        pass
                    with open(user+"/temp.dat", "wb")as f:
                        f.write(fullmsg)
                    """with open(user+"/temp.dat", "rb")as f:
                        e = load(f)
                        print(e)"""
                    if (verifcation_exist(user+"/temp.dat")):
                        conn.send("valid".encode("utf-8"))
                    else:
                        conn.send("notvalid".encode("utf-8"))
                elif sepa == "login":
                    fils = fullmsg.decode("utf-8")
                    a = fils[:fils.find("|*|")]
                    bs = fils[fils.find("|*|")+3:]
                    with open("test.txt", "w")as f:
                        f.write(a+"\n"+bs)
                    print(user_exist(a, bs))

                    if (user_exist(a, bs)):
                        useinfo = "valid"+get_userinfo(a, bs)
                        conn.send(useinfo.encode("utf-8"))
                    else:
                        conn.send("vanotlid".encode("utf-8"))

    conn.close()
    print("connection closed")


def start():
    server.listen()
    while True:
        con, adr = server.accept()
        ths = threading.Thread(target=handel, args=(con, adr))
        ths.start()
        print("[thread started]", threading.active_count()-1)


print("[server is starting]")
for i in tqdm(range(100)):
    time.sleep(0.1)
os.system("cls")

print("[server is online]")
start()
