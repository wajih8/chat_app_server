from sys import stdout
from json import dumps, loads
import sys
from verifcation import verifcation_exist
from pickle import dump
from func import *

xa = loads(sys.argv[1])

with open("temp/temp.dat", "wb")as f:
    dump(xa, f)
asf = verifcation_exist("temp/temp.dat")
if (asf == "user is valid"):
    e = {"wa": "true"}
else:
    e = {"wa": asf}


print(dumps(e))
stdout.flush()
