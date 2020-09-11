import logging
import os
from datetime import datetime


# # 项目路径
prj_path = os.path.dirname(os.path.abspath(__file__)) #当前文件的绝对路径的上一级，__file__指当前文件
'''
os.path.abspath(__file__) 当前文件的绝对路径,
os.path.dirname(os.path.abspath(__file__)) 当前目录的上一级的绝对路径
'''
# test_path = prj_path
date_time = str(datetime.now().strftime("%Y%m%d%H%M%S"))
log_file = os.path.join(prj_path, 'log', 'log.txt')
report_file = os.path.join(prj_path, 'report', 'report.html')
# log_file = os.path.join(prj_path, 'log', 'log'+date_time+'.txt')
# report_file = os.path.join(prj_path, 'report', '接口自动化测试报告'+date_time+'.html')
excel_Path = os.path.join(prj_path,'data','海佳单位接口测试用例.xls')
save_excel_Path = os.path.join(prj_path, 'report', '海佳单位接口测试用例结果'+date_time+'.xls')


# log配置
#将日志同时输出到文件和屏幕
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='w')  # w覆盖模式，a追加模式

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# 地址
HOST = 'http://47.99.212.180:8085/'
