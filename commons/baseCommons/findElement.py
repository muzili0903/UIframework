"""
@Time ： 2021/7/12 20:27
@Auth ： muzili
@File ： findElement.py
@IDE  ： PyCharm
"""
from abc import ABCMeta, abstractmethod


class FindElement(metaclass=ABCMeta):

    @abstractmethod
    def by_id(self, *args, **kwargs): pass

    @abstractmethod
    def by_name(self, *args, **kwargs): pass

    @abstractmethod
    def by_class(self, *args, **kwargs): pass

    @abstractmethod
    def by_tag(self, *args, **kwargs): pass

    @abstractmethod
    def by_link(self, *args, **kwargs): pass

    @abstractmethod
    def by_partial_link(self, *args, **kwargs): pass

    @abstractmethod
    def by_xpath(self, *args, **kwargs): pass

    @abstractmethod
    def by_css(self, *args, **kwargs): pass


class FindElements(metaclass=ABCMeta):

    @abstractmethod
    def by_id(self, *args, **kwargs): pass

    @abstractmethod
    def by_name(self, *args, **kwargs): pass

    @abstractmethod
    def by_class(self, *args, **kwargs): pass

    @abstractmethod
    def by_tag(self, *args, **kwargs): pass

    @abstractmethod
    def by_link(self, *args, **kwargs): pass

    @abstractmethod
    def by_partial_link(self, *args, **kwargs): pass

    @abstractmethod
    def by_xpath(self, *args, **kwargs): pass

    @abstractmethod
    def by_css(self, *args, **kwargs): pass
