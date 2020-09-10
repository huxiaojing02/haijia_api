import json
from conifig import *


def log_casxe_info(case_name, url, data, expect_res):
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)  # 如果data是dict类型，转换成字符串
    print('url',url)
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
