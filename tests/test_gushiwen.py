#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import os
from ddt import data, unpack, ddt

from commons.common import get_data_dict
from commons.webDriverOperator import WebDriverOperator
from commons.browserOperator import BrowserOperator


@ddt
class Test(unittest.TestCase):

    filename = os.path.basename(__file__)
    read, write, data_dict = get_data_dict(filename)

    def setUp(self):
        self.browser = BrowserOperator()
        self.driver = self.browser.open_url()
        self.wdo = WebDriverOperator(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    @data(*data_dict)
    @unpack
    def test_20210907220051(self, username, password):
        self.wdo.input_text('id', 'email', content=username)  # 输入账号
        self.wdo.input_text('id', 'pwd', content=password)  # 输入账号
        self.wdo.save_input(tp='xp', element='//*[@id="aspnetForm"]/div[4]/div[5]/a[1]', filename=Test.filename, read=Test.read, write=Test.write)  # 输入账号
        self.wdo.save_result(content='登录古诗文网站', filename=Test.filename, read=Test.read, write=Test.write)  # 输入账号


if __name__ == '__main__':
    pass
