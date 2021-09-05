"""
@Time ： 2021/7/27 22:32
@Auth ： muzili
@File ： test.py
@IDE  ： PyCharm
"""
import unittest
from ddt import data, unpack, ddt

def get_data():
    return [{'content': '1', 'code': '2'},
                 {'content': '11', 'code': '22'}]

@ddt
class Test(unittest.TestCase):
    data_dict = get_data()

    def tearDown(self):
        pass

    def setUp(self):
        pass

    @data(*data_dict)
    @unpack
    def test_1(self, code, content):
        print(content)
        print(code)


if __name__ == "__main__":
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test.test_1)
    run = unittest.TextTestRunner()
    run.run(suite)
