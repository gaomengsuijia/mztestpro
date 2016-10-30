#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest
import time

test_dir = './bbs/test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='login*.py')

if __name__ == "__main__":
    filename = "./bbs/report/result" + str(time.time()) + ".html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况")
    #runner = unittest.TextTestRunner()
    runner.run(discover)
    fp.close()