"""
@Time ： 2021/7/28 21:38
@Auth ： muzili
@File ： report.py
@IDE  ： PyCharm
"""
import time
import unittest

from commons.HTMLTestRunner import HTMLTestRunner
from commons.getFileDirs import REPORT, TESTS


class TestRunner(object):
    """自动生成测试报告"""

    def __init__(self, title=u'自动化测试报告', description=u'windows 7'):
        self.title = title
        self.des = description

    def run(self):
        now = time.strftime("%Y%m%d%H%M%S")
        fp = open(REPORT + '\\' + self.title + now + "report.html", 'wb')
        suite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(TESTS, pattern='test_*.py', top_level_dir=None)
        suite.addTests(discover)
        title = self.title + " auto test report"
        des = "环境：" + self.des
        runner = HTMLTestRunner(stream=fp, title=title, description=des)
        runner.run(suite)
        fp.close()


if __name__ == '__main__':
    test = TestRunner(title='古诗文')
    test.run()
