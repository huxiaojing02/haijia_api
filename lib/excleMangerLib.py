import xlrd
from lib.sendUnitRequestLib import *
from xlutils.copy import copy


def readExcel(excelPath, sheetName):
    workbook = xlrd.open_workbook(excelPath)
    worksheet = workbook.sheet_by_name(sheetName)
    # 计量单位表中有几行数据
    nrows = worksheet.nrows
    # 计量单位表中循环取出每一行数据
    listData = []
    for i in range(1, nrows):
        # 循环出来的数据添加在列表中
        listData.append(worksheet.row_values(i))
    return listData


def getNewExcel(excelPath):
    # formatting_info=True保留样式，对xlsx格式的不太支持，支持xls格式
    workBoork = xlrd.open_workbook(excelPath, formatting_info=True)
    copyWorkBoork = copy(workBoork)

    return copyWorkBoork


if __name__ == "__main__":
    list = readExcel(excel_Path, '计量单位')
    # 得到一个新的工作簿
    newWorkExcel = getNewExcel(excel_Path)
    # 操作新的工作簿里面的工作表
    copyWorkSheet = newWorkExcel.get_sheet(0)
    for i in range(0, len(list)):
        rows = list[i]
        resData = sendUnitRequest(rows)
        # 在弟10、11行写结果
        assertData = json.loads(rows[9])
        if resData['status'] == assertData['status']:
            print(rows[0], '新增测试通过')
            copyWorkSheet.write(i + 1, 10, "PASS")
        else:
            print(rows[0], '新增测试失败')
            copyWorkSheet.write(i + 1, 10, "FAIL")
            if 'message' in resData.keys():
                copyWorkSheet.write(i + 1, 11, resData['message'])
            else:
                copyWorkSheet.write(i + 1, 11, '没有message属性')
        # print('resData',resData)
        # excelResData = []
        # excelResData.append(resData)
        # print('excelResData',excelResData)

        # 保存
        newWorkExcel.save(save_excel_Path)
