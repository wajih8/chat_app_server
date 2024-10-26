from sys import stdout
from json import dumps, loads
import sys
from verifcation import verifcation_exist, user_exist
from pickle import dump
from func import *
from functionsa import get_userinfo
xa = loads(sys.argv[1])

if (user_exist(xa["user"], xa["password"])):
    e = dict()
    e = get_userinfo(xa["user"], xa["password"])
    e["wa"] = "true"
else:
    e = {"wa": "false"}


print(dumps(e))
stdout.flush()
