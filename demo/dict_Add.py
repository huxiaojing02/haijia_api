import requests
from conifig import *

hearData = {"auth-token": "5968bdc07ac8460c843f3793674d2efe",
            "Content-Type": "application/json"}
addData = """{
"code": "879",
"isBase": true,
"name": "千克1",
"preci": 0,
"sortNum": 1
} """
r = requests.post(f'{HOST}/unit/save', data=addData.encode(), headers=hearData)
