"""
@Time ： 2021/7/12 22:38
@Auth ： muzili
@File ： waitElement.py
@IDE  ： PyCharm
"""
from abc import abstractmethod, ABCMeta


class WaitElement(metaclass=ABCMeta):

    @abstractmethod
    def display_id(self, *args, **kwargs): pass  # id显示等待

    @abstractmethod
    def display_name(self, *args, **kwargs): pass  # name显示等待

    @abstractmethod
    def display_class(self, *args, **kwargs): pass  # class显示等待

    @abstractmethod
    def display_xpath(self, *args, **kwargs): pass  # xpath显示等待

    @abstractmethod
    def display_css(self, *args, **kwargs): pass  # css显示等待

    @abstractmethod
    def hide_wait_element(self, *args, **kwargs): pass  # 隐式等待
