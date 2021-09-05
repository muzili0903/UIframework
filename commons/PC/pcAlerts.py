"""
@Time ： 2021/7/17 15:08
@Auth ： muzili
@File ： pcAlerts.py
@IDE  ： PyCharm
"""
from selenium.common.exceptions import NoAlertPresentException, NoSuchFrameException
from selenium.webdriver.support.select import Select

from commons.baseCommons.alert import Alerts
from commons.common import get_png
from commons.logs import Logging

logger = Logging()


class PCAlerts(Alerts):

    def __init__(self, d):
        self.driver = d

    def accept(self, *args, **kwargs):
        """
        确定弹框
        :param args:
        :param kwargs:
        :return:
        """
        try:
            self.driver.switch_to.alert().accept()
        except NoAlertPresentException:
            get_png(self.driver)
            logger.err().error("Message: no such alert")
            return False
        return True

    def dismiss(self, *args, **kwargs):
        """
        忽略弹框
        :param args:
        :param kwargs:
        :return:
        """
        try:
            self.driver.switch_to.alert().dismiss()
        except NoAlertPresentException:
            get_png(self.driver)
            logger.err().error("Message: no such alert")
            return False
        return True

    def set_prompt(self, value):
        """
        设置弹框内容
        :param value:
        :return:
        """
        if value is None:
            value = "没有输入内容"
        try:
            self.driver.switch_to.alert().send_keys(value).accept()
        except NoAlertPresentException:
            get_png(self.driver)
            logger.err().error("Message: no such alert")
            return False
        return True

    def get_prompt(self, *args, **kwargs):
        """
        获取弹框内容
        :param args:
        :param kwargs:
        :return:
        """
        try:
            message = self.driver.switch_to.alert().text
        except NoAlertPresentException:
            get_png(self.driver)
            logger.err().error("Message: no such alert")
            return False
        return message

    def enter_frame(self, element):
        """
        进入frame
        :param element:
        :return:
        """
        if element is False:
            logger.err().error("进入frame失败，定位不到元素")
            return False

        try:
            self.driver.switch_to.frame(element)
        except NoSuchFrameException:
            get_png(self.driver)
            logger.err().error("进入frame失败，定位不到元素")
            return False
        return True

    def parent_frame(self):
        """
        返回上一层frame
        :return:
        """
        self.driver.switch_to.parent_frame()
        return True

    def quit_frame(self):
        """
        返回主页面
        :return:
        """
        self.driver.switch_to.default_content()
        return True

    def select_radio(self, element):
        """
        勾选单选框
        :param element:
        :return:
        """
        if element is False:
            logger.err().error("Message: no such element")
            return False
        if element.is_selected():
            return True
        else:
            element.click()
            return True

    def select_checkbox(self, element):
        """
        勾选多选框
        :param element:
        :return:
        """
        if element is False:
            logger.err().error("Message: no such element")
            return False
        if element.is_selected():
            return True
        else:
            element.click()
            return True

    def select_all_checkbox(self, elements):
        """
        勾选所有多选框
        :param elements:
        :return:
        """
        if elements is False:
            logger.err().error("Message: no such element")
            return False
        for element in elements:
            element.click()
        return True

    def deselect_checkbox(self, element):
        """
        取消多选框
        :param element:
        :return:
        """
        if element is False:
            logger.err().error("Message: no such element")
            return False
        if element.is_selected():
            element.click()
            return True
        else:
            return True

    def select_multi(self, element, value, tp):
        """
        勾选复选框
        :param element:
        :param tp:
        :param value:
        :return:
        """
        if element is False:
            logger.err().error("Message: no such element")
            return False

        select = Select(element)
        tp = tp.lower()
        if tp == 'text':
            select.select_by_visible_text(value)
        elif tp == 'value':
            select.select_by_value(value)
        elif tp == 'index':
            select.select_by_index(value)
        else:
            logger.err().error('Message: select only support text、value、index')
            return False
        return True

    def deselect_multi(self, element, value, tp):
        """
        勾选复选框
        :param element:
        :param tp:
        :param value:
        :return:
        """
        if element is False:
            logger.err().error("Message: no such element")
            return False

        select = Select(element)
        tp = tp.lower()
        if tp == 'text':
            select.deselect_by_visible_text(value)
        elif tp == 'value':
            select.deselect_by_value(value)
        elif tp == 'index':
            select.deselect_by_index(value)
        else:
            logger.err().error('Message: deselect only support text、value、index')
            return False
        return True

    def deselect_all_multi(self, element):
        """
        取消所有复选框
        :param element:
        :return:
        """
        select = Select(element)
        select.deselect_all()
        return True

    def select_single(self, element, value, tp):
        """
        勾选下拉框
        :param element:
        :param value:
        :param tp:
        :return:
        """
        if element is False:
            logger.err().error("Message: no such element")
            return False

        select = Select(element)
        tp = tp.lower()
        if tp == 'text':
            select.select_by_visible_text(value)
        elif tp == 'value':
            select.select_by_value(value)
        elif tp == 'index':
            select.select_by_index(value)
        else:
            logger.err().error('Message: select only support text、value、index')
            return False
        return True

    def select_window(self, index):
        """
        切换窗口
        :param index:
        :return:
        """
        try:
            all_handles = self.driver.window_handles
            self.driver.switch_to.window(all_handles[index])
        except IndexError:
            get_png(self.driver)
            logger.err().error('下标超出范围')
