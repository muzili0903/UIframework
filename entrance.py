"""
@Time ： 2021/8/23 20:45
@Auth ： muzili
@File ： entrance.py
@IDE  ： PyCharm
"""
from commons.common import get_all_file, write_file
from commons.getFileDirs import SCRIPTS
from commons.report import TestRunner

file_path = get_all_file(SCRIPTS)
for file in file_path:
    write_file(file)
test = TestRunner()
test.run()

if __name__ == "__main__":
    pass
