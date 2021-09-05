"""
@Time ： 2021/9/3 21:39
@Auth ： muzili
@File ： excel.py
@IDE  ： PyCharm
"""
from abc import ABCMeta, abstractmethod


class Write(metaclass=ABCMeta):

    @abstractmethod
    def post_cell(self, *args, **kwargs): pass  # 写单元格值


class Read(metaclass=ABCMeta):

    @abstractmethod
    def get_rows(self, *args, **kwargs): pass  # 获取一行的所有值

    @abstractmethod
    def get_cols(self, *args, **kwargs): pass  # 获取一列的所有值

    @abstractmethod
    def get_cell(self, *args, **kwargs): pass  # 获取单元格的值

    @abstractmethod
    def get_row_index(self, *args, **kwargs): pass  # 获取cell的行号
