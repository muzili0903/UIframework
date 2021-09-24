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
    def test_20210924233029(self, f_content):
        self.wdo.click('xp', '//*[@id="app"]/div/div[2]/div[3]/div[1]')  # 点击案例管理
        self.wdo.click('xp', '//*[@id="app"]/div/div[2]/div[3]/div[3]')  # 点击案例自动生成
        self.wdo.click('xp', '//*[@id="app"]/div/div[3]/div[5]/div[2]/div[1]')  # 点击新增
        self.assertIn('12', f_content, msg='12313')  # 点击新增
        self.assertEqual('12', '12', msg='12313')  # 点击新增


if __name__ == '__main__':
    pass
