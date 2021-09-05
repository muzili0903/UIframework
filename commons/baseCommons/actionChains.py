"""
@Time ： 2021/7/12 20:49
@Auth ： muzili
@File ： actionChains.py
@IDE  ： PyCharm
"""
from abc import abstractmethod, ABCMeta


class ActionChain(metaclass=ABCMeta):

    @abstractmethod
    def click(self, *args, **kwargs): pass  # 点击

    @abstractmethod
    def click_and_hold(self, *args, **kwargs): pass  # 在元素上按住鼠标左键

    @abstractmethod
    def right_click(self, *args, **kwargs): pass  # 在元素上执行上下文单击

    @abstractmethod
    def double_click(self, *args, **kwargs): pass  # 双击一个元素

    @abstractmethod
    def drag_and_drop(self, *args, **kwargs): pass  # 在源元素上按住鼠标左键，然后移动到目标元素并释放鼠标按钮

    @abstractmethod
    def drag_and_drop_by_offset(self, *args, **kwargs): pass  # 在源元素上按住鼠标左键，然后移动到目标偏移并释放鼠标按钮

    @abstractmethod
    def key_board(self, *args, **kwargs): pass  # 仅发送按键，不释放。只能与修饰键（Control、Alt 和 Shift）一起使用

    @abstractmethod
    def move_by_offset(self, *args, **kwargs): pass  # 将鼠标移动到与当前鼠标位置的偏移处

    @abstractmethod
    def move_to_element(self, *args, **kwargs): pass  # 将鼠标移动到元素的中间

    @abstractmethod
    def move_to_element_with_offset(self, *args, **kwargs): pass  # 将鼠标移动指定元素的偏移量。偏移量相对于元素的左上角

    @abstractmethod
    def pause(self, *args, **kwargs): pass  # 在指定的持续时间内暂停所有输入（以秒为单位）

    @abstractmethod
    def perform(self, *args, **kwargs): pass  # 执行所有存储的操作

    @abstractmethod
    def release(self, *args, **kwargs): pass  # 在元素上释放按住的鼠标按钮

    @abstractmethod
    def reset_actions(self, *args, **kwargs): pass  # 清除已存储在本地和远程端的操作

    @abstractmethod
    def send_keys(self, *args, **kwargs): pass  # 将键发送到当前聚焦的元素

    @abstractmethod
    def clear_and_send_keys(self, *args, **kwargs): pass  # 删除默认值再输入内容

    @abstractmethod
    def send_keys_to_element(self, *args, **kwargs): pass  # 将键发送到元素

    @abstractmethod
    def get_ele_text(self, *args, **kwargs): pass  # 下拉框
