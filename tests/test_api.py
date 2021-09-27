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

    def test_20210927214054(self):
        self.wdo.click('xp', '//*[@id="app"]/div/div[2]/div[3]/div[1]')  # 点击案例管理
        self.wdo.click('xp', '//*[@id="app"]/div/div[2]/div[3]/div[3]')  # 点击案例自动生成
        self.wdo.click('xp', '//*[@id="app"]/div/div[3]/div[5]/div[2]/div[1]')  # 点击新增
        self.wdo.click('xp', '//*[@id="app"]/div/div[3]/div[5]/div[3]/div[3]/div/div/div[2]/div[1]/form/div[1]/div[7]/div/div[2]/div/div[2]/span/i')
        self.wdo.click('xp', '/html/body/div[2]/div/div[2]')  # oracle
        self.wdo.input_text('xp', '//*[@id="app"]/div/div[3]/div[5]//div/div/div[2]/div[1]/form/div[1]/div[2]//div/input', '192.168.32.123')
        self.wdo.input_text('xp', '//*[@id="app"]/div/div[3]/div[5]/div[3]/div[3]/div/div/div[2]/div[1]/form/div[1]/div[3]/div/div[2]/div/input', '3306')


if __name__ == '__main__':
    pass
