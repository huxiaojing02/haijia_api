from lib.unitLib import add_unit, list_unit
import pprint

# 1、通过新增返回的id判断新增是否通过
unitAddRes = add_unit("kggr78873", "千克11434241", "true", 0, 3)
if unitAddRes['res'] != None:
    print('测试通过')
    unitAddId = unitAddRes["res"]
else:
    print('测试不通过')

unitListRes = list_unit("",1, 20)
pprint.pprint('unitListRes',unitListRes['res'])
for item in unitListRes['res']:
    item['id'] == unitAddId
    print('新增成功，id存在list列表中')
    break
else:
    print('新增失败，新增id不存在list列表中')