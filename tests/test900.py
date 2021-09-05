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
    data_dict = get_data_dict(filename)

    def setUp(self):
        self.browser = BrowserOperator()
        self.driver = self.browser.open_url()
        self.wdo = WebDriverOperator(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    @data(*data_dict)
    @unpack
    def test_20210902214625(self, content, fa_cont, fa_cont1, fa_cont2):
        self.wdo.confirm()
        self.wdo.parent_frame()  # 返回上一层
        self.wdo.save('id', 'email', content='test900.py&2584167983')  # 输入账号
        self.wdo.multi('id', 'email', content=fa_cont, s_tp='value')  # 输入账号
        self.wdo.multi('id', 'email', content=fa_cont1, s_tp='value')  # 输入账号
        self.wdo.multi('id', 'email', content=fa_cont2, s_tp='value')  # 输入账号
        self.wdo.input_text('id', 'email', content=content)  # 输入账号


if __name__ == '__main__':
    pass
