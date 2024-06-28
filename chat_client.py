from socket import *
import time
discp = "!disco".encode("utf-8")
discp += b" "*(64-6)
add = ('169.254.157.169', 6030)
client = socket(AF_INET, SOCK_STREAM)
while True:
    try:
        client.connect(add)
        break
    except:
        print("can't connect")
        time.sleep(5)

with open("indenti.dat", "rb")as f:
    file = f.read()
    b = "verlogin|"
    a = "verlogin|".encode("utf-8")
    a += b" "*(64-len(b))
    client.send(a)
    client.send(file)
    time.sleep(1)
    client.send(discp)
    time.sleep(1)
    x = client.recv(30).decode("utf-8")
    if x == "valid":
        print("valid")
    else:
        print("probloc")
