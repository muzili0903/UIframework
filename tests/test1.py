"""
@Time ： 2021/7/28 22:54
@Auth ： muzili
@File ： test900.py
@IDE  ： PyCharm
"""
import os

from commons.getConfig import Config
from commons.glo import GolStatic
from commons.logs import Logging

"""
GolStatic.set_file_temp('test1', 'test', '1')
GolStatic.set_file_temp('test1', 'test1', '11')
GolStatic.set_file_temp('test1', 'test1', '5551')
GolStatic.set_file_temp('test2', 'test2', '21')
GolStatic.set_file_temp('test2', 'test2', '22')

print(GolStatic.get_file_temp('test1', 'test'))
print(GolStatic.get_file_temp('test1', 'test1'))
print(GolStatic.get_file_temp('test2', 'test'))
print(GolStatic.get_file_temp('test2', 'test2'))

dic = dict()
dic['1'] = [{1: 1}]
dic['1'].append({1: 2})
print(dic)

import re

r = re.compile(r'^(@[\w]+\[[\w]+\]$)')
st = '@content[file_name]'
m = r.match(st)
print(m.group())
st1 = re.findall('^@([\w]+)\[(\w+)\]$', st)
print(type(st1))
print(st1[0][1])

GolStatic.set_script_temp('test1', 'test1')
GolStatic.set_script_temp('test1', 'test')

di = dict()
k = di.keys()
print(len(k))

print(GolStatic.get_script_temp('test1'))
print(GolStatic.get_script_temp('test1'))
"""
logger = Logging()
info = logger.info()
err = logger.err()

d = list()


def te():
    info.info('1111111')
    info.error('2111122')
    err.error('2111122')


for dd in d:
    print(dd)

lis = [11, 2, 3]
l1, l2, l3 = lis
print(lis.__contains__(1))
l = """saveInput={'xp':'//*[#id="aspnetForm"]/div[4]/div[5]/a[1]'}#输入账号}"""
for li in l.split('#', 2):
    print(li)
te()
conf = Config()
print(conf.get_config('report', 'envir1onment'))
print(conf.get_config('report', 'envir1onment'))
test = str()
print('test:', test)

s = '  '
if s.strip() == '':
    print('s is null')
print(s.strip())
