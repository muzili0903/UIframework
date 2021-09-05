"""
@Time ： 2021/7/27 22:02
@Auth ： muzili
@File ： tes1t_login.py
@IDE  ： PyCharm
"""
import unittest

from commons.webDriverOperator import WebDriverOperator
from commons.browserOperator import BrowserOperator


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserOperator()
        cls.driver = cls.browser.open_url()
        cls.wdo = WebDriverOperator(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close_browser()

    def setUp(self):
        pass
        # self.browser = BrowserOperator()
        # self.driver = self.browser.open_url()
        # self.wdo = WebDriverOperator(self.driver)

    def test_sign(self):
        self.wdo.input_text('id', 'email', content='2584167983@qq.com')
        self.wdo.input_text('id', 'pwd', 'yihong.li')
        code = input('请输入验证码：')
        self.wdo.input_text('id', 'code', content=code)
        self.wdo.click('id', 'denglu')
        text = self.wdo.get_text('cls', 'searchleft')
        self.assertIn('名句', text)

    def test_sign1(self):
        self.wdo.click('xp', '//*[@id="mainSearch"]/div[2]/div/div[1]/a')
        self.wdo.window(1)
        text = self.wdo.get_text('id', 'fanyi1384')
        self.assertIn('译文', text)

    def tearDown(self):
        pass
        # self.browser.close_browser()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login.test_sign)
    runner = unittest.TextTestRunner()
    runner.run(suite)
