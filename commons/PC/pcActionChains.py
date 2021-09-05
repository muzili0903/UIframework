"""
@Time ： 2021/7/15 20:41
@Auth ： muzili
@File ： pcActionChains.py
@IDE  ： PyCharm
"""
from selenium.webdriver.common.keys import Keys

from commons.PC.pcFindElement import PCFindElements
from commons.PC.pcWaitElement import PCWaitElement
from commons.baseCommons.actionChains import ActionChain
from commons.browserOperator import BrowserOperator
from selenium.webdriver.common.action_chains import ActionChains

from commons.logs import Logging

logger = Logging()


class PCActionChains(ActionChain):

    def __init__(self, d):
        self.driver = d

    def click(self, element):
        """
        单击
        :param element:
        :return:
        """
        if element is not False:
            element.click()
        else:
            logger.err().error("元素不存在，点击失败")

    def click_and_hold(self, element):
        """
        在元素上按住鼠标左键
        :param element:
        :return:
        """
        if element is not False:
            ActionChains(self.driver).click_and_hold(element).perform()
        else:
            logger.err().error("元素不存在，按住鼠标左键失败")

    def right_click(self, element):
        """
        右击
        :param element:
        :return:
        """
        if element is not False:
            ActionChains(self.driver).context_click(element).perform()
        else:
            logger.err().error("元素不存在，右击失败")

    def double_click(self, element):
        """
        双击
        :param element:
        :return:
        """
        if element is not False:
            ActionChains(self.driver).double_click(element).perform()
        else:
            logger.err().error("元素不存在，双击失败")

    def drag_and_drop(self, element, target):
        """
        在源元素上按住鼠标左键，然后移动到目标元素并释放鼠标按钮
        :param element:
        :param target:
        :return:
        """
        if element is not False:
            try:
                ActionChains(self.driver).drag_and_drop(element, target).perform()
            except Exception as e:
                logger.err().error(e, "目标元素不存在")
        else:
            logger.err().error("元素不存在，拖动失败")

    def drag_and_drop_by_offset(self, element, x, y):
        """
        按住元素移动到目标偏移量
        :param element:
        :param x:
        :param y:
        :return:
        """
        if type(x) is not int or type(y) is not int:
            logger.err().error("x 或 y 传参类型有误")
            return False
        if element is not False:
            ActionChains(self.driver).drag_and_drop_by_offset(element, x, y).perform()
        else:
            logger.err().error("元素不存在，移动失败")

    def key_board(self, key=None, value="c"):
        """
        快捷键
        :param key:
        :param value:
        :return:
        """
        value = value.lower()
        if key is None:
            key = Keys.CONTROL
        else:
            key = 'Keys' + '.' + key
        ActionChains(self.driver).key_down(key).send_keys(value).key_up(key).perform()

    def move_by_offset(self, x, y):
        """
        将鼠标移动到与当前鼠标位置的偏移处
        :param x:
        :param y:
        :return:
        """
        if type(x) is not int or type(y) is not int:
            logger.err().error("x 或 y 传参类型有误")
            return False
        ActionChains(self.driver).move_by_offset(x, y).perform()

    def move_to_element(self, element):
        """
        对定位到的元素执行悬停操作
        :param element:
        :return:
        """
        if element is not False:
            ActionChains(self.driver).move_to_element(element).perform()
        else:
            logger.err().error("元素不存在，悬停失败")

    def move_to_element_with_offset(self, element, x, y):
        """
        将鼠标移动指定元素的偏移量。偏移量相对于元素的左上角
        :param element:
        :param x:
        :param y:
        :return:
        """
        if type(x) is not int or type(y) is not int:
            logger.err().error("x 或 y 传参类型有误")
            return False
        if element is not False:
            ActionChains(self.driver).move_to_element_with_offset(element, x, y).perform()
        else:
            logger.err().error("元素不存在，移动失败")

    def pause(self, element, seconds=5):
        """
        暂停，默认暂停5秒
        :param element:
        :param seconds:
        :return:
        """
        if element is not False:
            ActionChains(self.driver).move_to_element(element).pause(seconds)
        else:
            logger.err().error("元素不存在，暂停失败")

    def perform(self, *args, **kwargs):
        pass  # 执行所有存储的操作

    def release(self, *args, **kwargs):
        """
        在元素上释放按住的鼠标按钮
        :param args:
        :param kwargs:
        :return:
        """
        ActionChains(self.driver).release()

    def reset_actions(self, *args, **kwargs):
        pass  # 清除已存储在本地和远程端的操作

    def send_keys(self, element, value="python"):
        """
        将键发送到当前元素
        :param element:
        :param value:
        :return:
        """
        if element is not False:
            element.send_keys(value)
        else:
            logger.err().error("元素不存在，发送失败")

    def clear_and_send_keys(self, element, value="python"):
        """
        先清除默认值，再输入内容
        :param element:
        :param value:
        :return:
        """
        if element is not False:
            element.clear()
            element.send_keys(value)
        else:
            logger.err().error("元素不存在，发送失败")

    def send_keys_to_element(self, element, value="python"):
        """
        将键发送到元素
        :param element:
        :param value:
        :return:
        """
        if element is not False:
            ActionChains(self.driver).send_keys_to_element(element, value).perform()
        else:
            logger.err().error("元素不存在，发送失败")

    def get_ele_text(self, element):
        """
        获取元素内容
        :param element:
        :return:
        """
        if element is False:
            logger.err().error("Message: no such element")
            return False
        return element.text


if __name__ == "__main__":
    driver = BrowserOperator()
    browser = driver.open_url(url="https://www.baidu.com")
    pc = PCFindElements(browser)
    wait = PCWaitElement(browser)
    wait.hide_wait_element()
    ac = PCActionChains(browser)
    ele = pc.by_id("kw")
    ac.move_to_element_with_offset(ele, "s", 3)
    # ac.click(pc.by_id("su"))
    # driver.close_browser()
