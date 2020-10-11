import requests
import pprint
from lib.caseLog import *


def add_unit(case_name, api, hearData, code, name, isBase, preci, sortNum):
    addData = f"""{{
        "code": "{code}",
        "name": "{name}",
        "isBase": {isBase},
        "preci": {preci},
        "sortNum": {sortNum}
        }}"""
    try:
        url = f'{HOST}' + api
        r = requests.post(url, data=addData.encode(), headers=hearData)
        log_casxe_info(case_name, url, addData, r.text)
        return r.json()
    except:
        logging.error({"status": 34434343, "message": "异常情况"})


def detail_unit(id, code, hearData, name, isBase, preci, sortNum):
    detailData = f"""{{
    "id": {id},
    "code": "{code}",
    "name": "{name}",
    "isBase": {isBase},
    "preci": {preci},
    "sortNum": {sortNum}
    }}"""
    r = requests.post(f'{HOST}/unit/save', data=detailData.encode(), headers=hearData)
    pprint.pprint(r.json())


def list_unit(case_name, api, hearData, name, pageIndex, pageSize):
    listData = f"""{{
    "name": "{name}",
    "pageIndex": {pageIndex},
    "pageSize": {pageSize}
    }}"""
    try:
        # r = requests.post(f'{HOST}/unit/list', data=listData, headers=hearData)
        url = f'{HOST}' + api
        r = requests.post(url, data=listData.encode(), headers=hearData)
        log_casxe_info(case_name, url, listData, r.text)
        return r.json()
    except:
        logging.error({"status": 34434343, "message": "异常情况"})

# if __name__ == "__main__":
#     add_unit("case_name",'unit/save',"kgg", "千克111", "true", 0, 3)
#     # detail_unit(38,"kgg", "千克11111", "true", 0, 3)
# list_unit( "",1, 20)
