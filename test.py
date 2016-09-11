

# coding=utf8
import sys
import time
from pymongo import MongoClient

import tick

if sys.version < "3":
    reload(sys)
    sys.setdefaultencoding("utf-8")

import time
import base64
from hashlib import sha1
from hmac import new as hmac
import json

if sys.version > "3":
    from urllib import request as http
else:
    import urllib2 as http


def create_token(access_key, secret_key):
    t = str(time.time())

    if sys.version > "3":
        token = base64.encodebytes(hmac(
            bytearray("%s,%s,%s" % (access_key, t, secret_key), "utf-8"), digestmod=sha1).digest())[:-1]
    else:
        token = base64.encodestring(hmac("%s,%s,%s" % (access_key, t, secret_key), digestmod=sha1).digest())[:-1]

    return t, token

ticklen = len(tick.tick)


access_key = 'ff994a517642b489aabe2af85c345380'
secret_key = 'gJnulfQ7k4SgVPZdJbbfECiGo3o='
t, token = create_token(access_key, secret_key)

header = {
    "access_key": access_key,
    "t": t,
    "token": token,
}

url = "http://api.ichinascope.com/api/stock/summary?code=601010"
req = http.Request(url, headers=header)
data = http.urlopen(req).read()
if isinstance(data, bytes):
    result = json.loads(data.decode("utf-8"))
else:
    result = json.loads(data)
try:
    conn = MongoClient('localhost', 27017)
    conn.db.test.insert(result['message'])
    conn.close()
except:pass

