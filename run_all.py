import unittest
from AqiHTMLTestRunner import HTMLTestRunner
from conifig import *

suit = unittest.defaultTestLoader.discover("demo", pattern="demo_ddt*.py")

resultPath = report_file
fp = open(resultPath, 'wb')
#
runner = HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
runner.run(suit)
