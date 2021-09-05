"""
@Time ： 2021/7/17 15:00
@Auth ： muzili
@File ： alert.py
@IDE  ： PyCharm
"""
from abc import ABCMeta, abstractmethod


class Alerts(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, *args, **kwargs): pass  # 确认提示框

    @abstractmethod
    def dismiss(self, *args, **kwargs): pass  # 忽略提示框

    @abstractmethod
    def set_prompt(self, *args, **kwargs): pass  # 输入对话框内容

    @abstractmethod
    def get_prompt(self, *args, **kwargs): pass  # 获取对话框内容

    @abstractmethod
    def enter_frame(self, *args, **kwargs): pass  # 进入frame

    @abstractmethod
    def parent_frame(self, *args, **kwargs): pass  # 返回上一层frame

    @abstractmethod
    def quit_frame(self, *args, **kwargs): pass  # 返回主页面

    @abstractmethod
    def select_radio(self, *args, **kwargs): pass  # 勾选单选框

    @abstractmethod
    def select_checkbox(self, *args, **kwargs): pass  # 勾选多选框

    @abstractmethod
    def select_all_checkbox(self, *args, **kwargs): pass  # 勾选所有多选框

    @abstractmethod
    def deselect_checkbox(self, *args, **kwargs): pass  # 取消多选框

    @abstractmethod
    def select_multi(self, *args, **kwargs): pass  # 勾选复选框

    @abstractmethod
    def deselect_multi(self, *args, **kwargs): pass  # 取消复选框

    @abstractmethod
    def deselect_all_multi(self, *args, **kwargs): pass  # 取消所有复选框

    @abstractmethod
    def select_single(self, *args, **kwargs): pass  # 下拉框

    @abstractmethod
    def select_window(self, *args, **kwargs): pass  # 下拉框
