import time
from lib.unitLib import *
from lib.loginLib import login


def sendUnitRequest(rows):
    case_name = str(rows[0])+'---'+rows[1]
    api = rows[2]
    loginToken = login("admin", "123456")
    hearData = json.loads(rows[4])
    hearData['auth-token'] = loginToken['res'] #将dict中的auth-token对应的value 替换成登录接口返回的token，其他键值对保持不变
    if rows[1] == "新增单位":
        unitData = json.loads(rows[8])
        time.sleep(0.001)
        unitNameStr = str(round(time.time() * 1000))
        name = unitData['name'].replace("{{unitName}}", unitNameStr)
        code = unitData['code']
        # 将取到的'True’，替换为'true'
        isBase = str(unitData['isBase']).replace(str(unitData['isBase']), "true")
        preci = int(unitData['preci'])
        sortNum = int(unitData['sortNum'])
        UnitData = add_unit(case_name, api, hearData, code, name, isBase, preci, sortNum)
        # if addUnitData['status'] == assertData['status']:
        #     print(rows[0], '新增测试通过')
        # else:
        #     print(rows[0], '新增测试失败')
    elif rows[1] == "单位列表":
        listData = json.loads(rows[8])
        UnitData = list_unit(case_name, api, hearData, listData['name'], listData['pageIndex'], listData['pageSize'])
        # if listUnitData['status'] == assertData['status']:
        #     print(rows[0], '列表测试通过')
        # else:
        #     print(rows[0], '列表测试失败')
        # print('UnitData', UnitData)
    return UnitData
