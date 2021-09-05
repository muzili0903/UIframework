"""
@Time ： 2021/8/4 21:00
@Auth ： muzili
@File ： common.py
@IDE  ： PyCharm
"""
import os
import re
from datetime import datetime

from commons.excelOperator import ReadXLS, ReadExcel
from commons.getFileDirs import SCREENSHOTS, TESTS, SCRIPTS, DATADIR
from commons.logs import Logging
from commons.methodMap import METHODS, ELE_TYPE
from commons.glo import GolStatic

logger = Logging()


def get_png(driver, filename=None):
    """
    截图
    :param driver:
    :param filename:
    :return:
    """
    if filename is None:
        filename = SCREENSHOTS + '\\' + datetime.now().strftime('%Y%m%d%H%M%S') + '.png'
    else:
        filename = SCREENSHOTS + '\\' + filename + datetime.now().strftime('%Y%m%d%H%M%S') + '.png'
    driver.get_screenshot_as_file(filename)
    return filename


def write_header(path):
    """
    写unittest文件头部
    :param path: unittest文件保存的路径
    :return:
    """
    str1 = """@ddt\nclass Test(unittest.TestCase):\n
    filename = os.path.basename(__file__)
    data_dict = get_data_dict(filename)\n
    def setUp(self):
        self.browser = BrowserOperator()
        self.driver = self.browser.open_url()
        self.wdo = WebDriverOperator(self.driver)\n"""
    str2 = """
    def tearDown(self):
        self.browser.close_browser()\n"""
    with open(path, "w", encoding='utf-8') as f_write:
        f_write.writelines("""#!/usr/bin/python\n# -*- coding: UTF-8 -*-\n""")
        f_write.write("import unittest\n")
        f_write.write("import os\n")
        f_write.write("from ddt import data, unpack, ddt\n\n")
        f_write.write("from commons.common import get_data_dict\n")
        f_write.write("from commons.webDriverOperator import WebDriverOperator\n")
        f_write.write("from commons.browserOperator import BrowserOperator\n\n\n")
        f_write.writelines(str1)
        f_write.writelines(str2)


def write_case(f_read, path):
    """
    写unittest文件主要部分
    :param f_read: 需要写的文件
    :param path: unittest文件保存的路径
    :return:
    """
    f_name = os.path.split(path)[1]
    lines = str()
    for line in f_read.readlines():
        line = "\n        " + dispose_line(line.strip(), f_name)
        lines = lines + line
    function_name = dispose_function(f_name)
    '''
    function_name = """
    def test_%s(self):""" % (datetime.now().strftime('%Y%m%d%H%M%S'))
    '''
    with open(path, "a+", encoding='utf-8') as f_write:
        f_write.writelines(function_name)
        f_write.writelines(lines)


def write_main(path):
    """
    写unittest文件尾部
    :param path: unittest文件保存的路径
    :return:
    """
    with open(path, "a+", encoding='utf-8') as f_write:
        f_write.writelines("""\n\n\n""")
        f_write.writelines("""if __name__ == '__main__':\n""")
        f_write.writelines("    pass\n")


def write_file(read_file):
    """
    写文件
    :param read_file:
    :return:
    """
    filename = None
    f_read = open(read_file, "r", encoding='utf-8')
    line = f_read.readline()
    if "create=True" in line:
        filename = get_file_name(read_file)
    if filename is None:
        f_read.close()
        return
    filename = TESTS + filename
    print('filename: ', filename)
    write_header(filename)
    write_case(f_read, filename)
    write_main(filename)
    f_read.close()


def get_all_file(path):
    """
    获取所有文件路径
    :param path:
    :return:
    """
    files_path = []
    files = os.listdir(path)
    for f in files:
        f_path = os.path.join(path, f)
        files_path.append(f_path)
    return files_path


def dispose_function(filename):
    """
    返回函数名称
    :param filename: 文件名称
    :return:
    """
    function_name = """
    @data(*data_dict)
    @unpack
    def test_%s(self""" % (datetime.now().strftime('%Y%m%d%H%M%S'))
    case_list = GolStatic.get_case_temp(filename)
    if case_list is not None:
        for case in case_list:
            function_name = function_name + ', ' + case
    script_list = GolStatic.get_script_temp(filename)
    print('script_list: ', script_list)
    if script_list is not None:
        for script in script_list:
            function_name = function_name + ', ' + script
    this_script_list = GolStatic.get_this_script_temp(filename)
    print('this_script_list: ', this_script_list)
    if len(this_script_list) > 0:
        for script_list in this_script_list:
            for script in script_list:
                function_name = function_name + ', ' + script
    print("dispose_function:", function_name + '):')
    return function_name + '):'


def dispose_line(line, filename):
    """
    处理每一行数据，返回写入py文件的每行代码
    :param line:
    :param filename:
    :return:
    """
    if '=' in line:
        method, dict_content = line.split('=')
        method = method.strip()
        contents = METHODS.get(method)
        if '#' in dict_content:
            dict_content, note = dict_content.split('#')
            dict_content = eval(dict_content.strip())
            tp, value = find_ele_type(dict_content)
            tp = "'" + tp + "'"
            value = "'" + value + "'"
            r_contents = contents.replace('tp', tp, 1).replace('element', value, 1)
            r_contents = find_content(dict_content, r_contents, filename)
            r_contents = find_s_tp(dict_content, r_contents) + "  # " + note.strip()
        else:
            dict_content = eval(dict_content.strip())
            tp, value = find_ele_type(dict_content)
            tp = "'" + tp + "'"
            value = "'" + value + "'"
            r_contents = contents.replace('tp', tp, 1).replace('element', value, 1)
            r_contents = find_content(dict_content, r_contents, filename)
        print(r_contents)
        return r_contents
    elif '#' in line:
        method, note = line.split('#')
        method = method.strip()
        print(METHODS.get(method) + "  # " + note.strip())
        return METHODS.get(method) + "  # " + note.strip()
    else:
        method = line.strip()
        print(METHODS.get(method))
        return METHODS.get(method)


def find_ele_type(dict_content):
    """
    返回定位类型以及元素
    :param dict_content:
    :return:
    """
    tp = None
    value = None
    for tp in ELE_TYPE:
        value = dict_content.get(tp)
        if value is not None:
            break
    if value is None:
        logger.err().error('定位类型传入错误')
        raise KeyError("定位类型传入错误")
    return tp, value


def find_content(dict_content, contents, filename):
    """
    返回替换后的content内容
    :param dict_content:
    :param contents:
    :param filename:
    :return:
    """
    content = dict_content.get('content')
    if content is None:
        return contents
    else:
        if content[0] == '$':  # 取excel表格数据
            c = content.split('$')[-1]
            content = 'content=' + c
            GolStatic.set_case_temp(filename, c)
            print('GolStatic.get_case_temp(file_name)', GolStatic.get_case_temp(filename))
        elif content[0] == '@':  # 取脚本数据
            # \w匹配字母数字及下划线
            pattern = re.compile(r'^(@[\w]+\[[\w]+\]$)')
            if pattern.match(content) is None:  # 取本脚本数据
                c = content.split('@')[-1]
                fc = 'f_' + c
                content = 'content=' + fc
                GolStatic.set_script_temp(filename, fc)
            else:  # 取指定脚本数据
                # 匹配返回 [(变量名，文件名)]
                res = re.findall('^@([\w]+)\[(\w+)\]$', content)
                fct = 'fa_' + res[0][0]
                content = 'content=' + fct
                key = filename + '_' + res[0][1]
                GolStatic.set_script_temp(key, fct)
        elif content[0] == '&':  # 存脚本数据
            c = content.split('&')[-1]
            content = 'content=' + "'" + filename + '&' + c + "'"
            print("content = 'content=' + filename + '_' + c", content.split('&'))
        else:  # 取传入数据
            content = "'" + content + "'"
        # r_contents = contents.replace('content', content, 1)
        return contents.replace('content', content, 1)


def find_s_tp(dict_content, contents):
    """
    替换s_tp的类型
    :param dict_content:
    :param contents:
    :return:
    """
    s_tp = dict_content.get('s_tp')
    if s_tp is None:
        return contents
    else:
        s_tp = "s_tp='" + s_tp + "'"
        # r_contents = contents.replace("s_tp='text'", s_tp, 1)
        return contents.replace("s_tp='text'", s_tp, 1)


def get_file_name(path):
    """
    获取文件名字
    :param path:
    :return:
    """
    return os.path.split(path)[1] + '.py'


def get_excel_data(path, filename):
    """
    获取案例的输入数据
    :param path: excel文件路径
    :param filename: 文件名为案例的用例编号
    :return:
    """
    values = list()
    if os.path.splitext(path)[1] == '.xlsx':
        read = ReadExcel(path)
    elif os.path.splitext(path)[1] == '.xls':
        read = ReadXLS(path)
    else:
        logger.err().error('文件类型传入错误')
        raise KeyError("文件类型传入错误")
    rows = read.get_row_index(col_x=1, value=filename)
    if len(rows) > 0:
        for row in rows:
            values.append(read.get_cell(row, col_x=13))
    return values


def get_data_dict(filename) -> list:
    """
    获取测试数据
    :param filename:
    :return:
    """
    data_dict = list()
    path = get_all_file(DATADIR)
    print(path)
    xls_data = get_excel_data(path[0], filename)
    if len(xls_data) > 0:
        for data in xls_data:
            d = dict()
            d_list = data.split('\n')
            print('d_list:', d_list)
            for kv in d_list:
                kv = kv.strip()
                k, v = kv.split('=')
                d[k] = v
            data_dict.append(d)
        print('data_dict: ', data_dict)
    script_list = GolStatic.get_script_temp(filename)
    print('script_list: ', script_list)
    if script_list is not None:
        if len(data_dict) > 0:
            for data in data_dict:
                for script in script_list:
                    # TODD 应该把 f_ 去掉再取值把？
                    data.update({script: GolStatic.get_file_temp(filename, script)})
        else:
            d = dict()
            for script in script_list:
                # TODD 应该把 f_ 去掉再取值把？
                d.update({script: GolStatic.get_file_temp(filename, script)})
            data_dict.append(d)
    this_script_list = GolStatic.get_this_script_temp(filename)
    print('this_script_list: ', this_script_list)
    if len(this_script_list) > 0:
        if len(data_dict) > 0:
            for data in data_dict:
                for script_list in this_script_list:
                    for script in script_list:
                        # TODD 应该把 fa_ 去掉再取值把？
                        data.update({script: GolStatic.get_file_temp(filename, script)})
        else:
            d = dict()
            for script_list in this_script_list:
                for script in script_list:
                    # TODD 应该把 fa_ 去掉再取值把？
                    d.update({script: GolStatic.get_file_temp(filename, script)})
            data_dict.append(d)
    print(data_dict)
    return data_dict


if __name__ == "__main__":
    file_path = get_all_file(SCRIPTS)
    for file in file_path:
        write_file(file)
    file_path = get_all_file(DATADIR)
    print(get_excel_data(file_path[0], 'test'))
    get_data_dict('test')
