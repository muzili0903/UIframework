"""
@Time ： 2021/7/12 22:02
@Auth ： muzili
@File ： pcFindElement.py
@IDE  ： PyCharm
"""
from commons.baseCommons.findElement import FindElement, FindElements
from commons.browserOperator import BrowserOperator
from commons.PC.pcWaitElement import PCWaitElement
from commons.common import get_png
from commons.logs import Logging

logger = Logging()


class PCFindElement(FindElement):

    def __init__(self, d):
        self.driver = d

    def by_id(self, element):
        """
        根据id查找 id="kw"
        :param element:
        :return:
        """
        try:
            element = self.driver.find_element_by_id(element)
        except Exception as e:
            logger.err().error(e)
            return False
        return element

    def by_name(self, element):
        """
        根据name查找 name="wd"
        :param element:
        :return:
        """
        try:
            element = self.driver.find_element_by_name(element)
        except Exception as e:
            logger.err().error(e)
            return False
        return element

    def by_css(self, element):
        """
        根据css查找 '#kw'
        :param element:
        :return:
        """
        try:
            element = self.driver.find_element_by_css_selector(element)
        except Exception as e:
            logger.err().error(e)
            return False
        return element

    def by_xpath(self, element):
        """
        根据xpath查找 //*[@id='kw']
        :param element:
        :return:
        """
        try:
            element = self.driver.find_element_by_xpath(element)
        except Exception as e:
            logger.err().error(e)
            return False
        return element

    def by_class(self, element):
        """
        根据class查找 class="s_ipt"
        :param element:
        :return:
        """
        try:
            element = self.driver.find_element_by_class_name(element)
        except Exception as e:
            logger.err().error(e)
            return False
        return element

    def by_link(self, element):
        """
        根据link查找 文本链接
        :param element:
        :return:
        """
        try:
            element = self.driver.find_element_by_link_text(element)
        except Exception as e:
            logger.err().error(e)
            return False
        return element

    def by_partial_link(self, element):
        """
        根据partial_link查找 截取部分文本链接
        :param element:
        :return:
        """
        try:
            element = self.driver.find_element_by_partial_link_text(element)
        except Exception as e:
            logger.err().error(e)
            return False
        return element

    def by_tag(self, element):
        """
        根据tag查找 div,input,a
        :param element:
        :return:
        """
        try:
            element = self.driver.find_element_by_tag_name(element)
        except Exception as e:
            logger.err().error(e)
            return False
        return element


class PCFindElements(FindElements):

    def __init__(self, d):
        self.driver = d

    def by_id(self, element):
        """
        根据id查找 id="kw"
        :param element:
        :return:
        """
        try:
            element = self.driver.find_elements_by_id(element)
        except Exception as e:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址:\n', screen)
            logger.err().error(e, "; Message: no such element")
            return False
        return element

    def by_name(self, element):
        """
        根据name查找 name="wd"
        :param element:
        :return:
        """
        try:
            element = self.driver.find_elements_by_name(element)
        except Exception as e:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址:\n', screen)
            logger.err().error(e, "; Message: no such element")
            return False
        return element

    def by_css(self, element):
        """
        根据css查找 '#kw'
        :param element:
        :return:
        """
        try:
            element = self.driver.find_elements_by_css_selector(element)
        except Exception as e:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址:\n', screen)
            logger.err().error(e, "; Message: no such element")
            return False
        return element

    def by_xpath(self, element):
        """
        根据xpath查找 //*[@id='kw']
        :param element:
        :return:
        """
        try:
            element = self.driver.find_elements_by_xpath(element)
        except Exception as e:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址:\n', screen)
            logger.err().error(e, "; Message: no such element")
            return False
        return element

    def by_class(self, element):
        """
        根据class查找 class="s_ipt"
        :param element:
        :return:
        """
        try:
            element = self.driver.find_elements_by_class_name(element)
        except Exception as e:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址:\n', screen)
            logger.err().error(e, "; Message: no such element")
            return False
        return element

    def by_link(self, element):
        """
        根据link查找 文本链接
        :param element:
        :return:
        """
        try:
            element = self.driver.find_elements_by_link_text(element)
        except Exception as e:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址:\n', screen)
            logger.err().error(e, "; Message: no such element")
            return False
        return element

    def by_partial_link(self, element):
        """
        根据partial_link查找 截取部分文本链接
        :param element:
        :return:
        """
        try:
            element = self.driver.find_elements_by_partial_link_text(element)
        except Exception as e:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址:\n', screen)
            logger.err().error(e, "; Message: no such element")
            return False
        return element

    def by_tag(self, element):
        """
        根据tag查找 div,input,a
        :param element:
        :return:
        """
        try:
            element = self.driver.find_elements_by_tag_name(element)
        except Exception as e:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址:\n', screen)
            logger.err().error(e, "; Message: no such element")
            return False
        return element


if __name__ == "__main__":
    driver = BrowserOperator()
    browser = driver.open_url(url="https://www.baidu.com")
    pc = PCFindElements(browser)
    wait = PCWaitElement(browser)
    ele = pc.by_id("su")
    logger.err().error(ele)
    ele = pc.by_partial_link("新")
    logger.err().error(ele)
    ele = pc.by_css("#su1")
    logger.err().error(ele)
    driver.close_browser()
