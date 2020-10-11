import requests
from haijia_api.conifig import HOST


headData = {"Content-Type": "application/json"}


def login(loginName, password):
    loginData = f"""{{
    "loginName":"{loginName}",
    "password": "{password}"
    }}"""
    r = requests.post(f'{HOST}/frame/user/login', data=loginData.encode(), headers=headData)
    return r.json()  # 字符串转字典
