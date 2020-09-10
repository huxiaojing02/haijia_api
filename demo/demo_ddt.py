import unittest
from lib.excleMangerLib import *
from ddt import ddt, data

excelData = readExcel(excel_Path, '计量单位')


@ddt
class ddtClass(unittest.TestCase):

    def setUp(self):
        print('setUp运行成功')

    def tearDown(self):
        print('tearDown运行成功')

    def test_001(self):
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
        print('r',r.json())

    @unittest.skip("不执行第二条用例 ")
    def test_002(self):
        print("test_002运行成功")

    def test_003(self):
        self.assertEqual(1, 2, '测试用例不通过')
        print("test_003运行不成功")

    @data(*excelData)
    def test_004(self, row):
        resData = sendUnitRequest(row)
        assertData = json.loads(row[9])
        print('resData', resData)
        if "message" in resData.keys():
            self.assertEqual(resData['status'], assertData['status'], resData['message'])
        print("test_004运行成功")