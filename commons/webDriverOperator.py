"""
@Time ： 2021/7/8 21:54
@Auth ： muzili
@File ： webDriverOperator.py
@IDE  ： PyCharm
"""
from commons.PC.pcActionChains import PCActionChains
from commons.PC.pcAlerts import PCAlerts
from commons.PC.pcFindElement import PCFindElements
from commons.PC.pcWaitElement import PCWaitElement
from commons.glo import GolStatic
from commons.logs import Logging

logger = Logging()


class WebDriverOperator(object):

    def __init__(self, driver):
        self.driver = driver
        self.ac = PCActionChains(self.driver)
        self.wait = PCWaitElement(self.driver)
        self.find = PCFindElements(self.driver)
        self.at = PCAlerts(self.driver)

    def _ele_type(self, tp, element, index=None):
        """
        根据tp类型进行定位element元素
        :param tp:
        :param element:
        :return:
        """
        tp = tp.lower()
        ele = False
        if tp == 'xp':
            if self.wait.display_xpath(element=element):
                ele = self.find.by_xpath(element)
        elif tp == 'id':
            if self.wait.display_id(element=element):
                ele = self.find.by_id(element)
        elif tp == 'css':
            if self.wait.display_css(element=element):
                ele = self.find.by_css(element=element)
        elif tp == 'cls':
            if self.wait.display_class(element=element):
                ele = self.find.by_class(element=element)
        elif tp == 'name':
            if self.wait.display_name(element=element):
                ele = self.find.by_name(element)
        elif tp == 'lk':
            ele = self.find.by_link(element)
        elif tp == 'plk':
            ele = self.find.by_partial_link(element)
        elif tp == 'tag':
            ele = self.find.by_tag(element)
        else:
            print('type not exist')
        if ele is not False and index is None:
            return ele[0]
        elif ele is not False and index == '-1':
            return ele
        elif ele is not False:
            return ele[index]
        else:
            return ele

    def clear_input_text(self, tp, element, content):
        """
        清除默认值，输入新内容
        :param tp:
        :param element:
        :param content:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.ac.clear_and_send_keys(ele, content)

    def input_text(self, tp, element, content):
        """
        输入内容
        :param tp:
        :param element:
        :param content:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.ac.send_keys(ele, content)

    def get_text(self, tp, element):
        """
        获取内容
        :param tp:
        :param element:
        :return:
        """
        ele = self._ele_type(tp, element)
        return self.ac.get_ele_text(ele)

    def click(self, tp, element):
        """
        点击按钮
        :param tp:
        :param element:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.ac.click(ele)

    def radio(self, tp, element):
        """
        单选
        :param tp:
        :param element:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.at.select_radio(ele)

    def single(self, tp, element, content, s_tp='text'):
        """
        下拉框
        :param tp: 元素定位类型
        :param element:
        :param content:
        :param s_tp: 下拉框类型
        :return:
        """
        ele = self._ele_type(tp, element)
        self.at.select_single(ele, content, s_tp)

    def checkbox(self, tp, element):
        """
        多选框选中其中一个元素
        :param tp:
        :param element:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.at.select_checkbox(ele)

    def checkbox_all(self, tp, elements):
        """
        多选框选中全部
        :param tp:
        :param elements:
        :return:
        """
        ele = self._ele_type(tp, elements, index='-1')
        self.at.select_all_checkbox(ele)

    def del_checkbox(self, tp, element):
        """
        取消选择的多选框
        :param tp:
        :param element:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.at.deselect_checkbox(ele)

    def multi(self, tp, element, content, s_tp='text'):
        """
        勾选复选框
        :param tp:
        :param element:
        :param content:
        :param s_tp:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.at.select_multi(ele, content, s_tp)

    def del_multi(self, tp, element, content, s_tp='text'):
        """
        取消复选框选中的值
        :param tp:
        :param element:
        :param content:
        :param s_tp:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.at.deselect_multi(ele, content, s_tp)

    def del_all_multi(self, tp, elements):
        """
        取消复选框所有选中的值
        :param tp:
        :param elements:
        :return:
        """
        ele = self._ele_type(tp, elements, index='-1')
        self.at.deselect_all_multi(ele)

    def confirm(self):
        """
        点击弹框确定按钮
        :return:
        """
        self.at.accept()

    def cancel(self):
        """
        点击弹框取消按钮
        :return:
        """
        self.at.dismiss()

    def frame(self, tp, element):
        """
        进入frame
        :param tp:
        :param element:
        :return:
        """
        ele = self._ele_type(tp, element)
        self.at.enter_frame(ele)

    def quit_frame(self):
        """
        退出frame,回到主页面
        :return:
        """
        self.at.quit_frame()

    def parent_frame(self):
        """
        返回上一层frame
        :return:
        """
        self.at.parent_frame()

    def window(self, index):
        """
        切换窗口
        :param index:
        :return:
        """
        self.at.select_window(index)

    def save(self, tp, element, content):
        """
        保存页面元素的值
        :param tp:
        :param element:
        :param content:
        :return:
        """
        ele = self._ele_type(tp, element)
        value = self.ac.get_ele_text(ele)
        filename, key = content.split('&')
        GolStatic.set_file_temp(filename=filename, key=key, value=value)

    def save_result(self):
        """
        保存结果到xls
        :return:
        """

    def save_input(self, **kwargs):
        """
        保存输入数据
        :return:
        """
        try:
            tp = kwargs['tp']
            element = kwargs['element']
            ele = self._ele_type(tp, element)
            value = self.ac.get_ele_text(ele)
        except KeyError:
            raise KeyError("tp或element不存在")
