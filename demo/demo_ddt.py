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
        print('test_001运行成功')

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