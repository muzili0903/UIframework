"""
@Time ： 2021/7/12 22:49
@Auth ： muzili
@File ： pcWaitElement.py
@IDE  ： PyCharm
"""
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from commons.baseCommons.waitElement import WaitElement
from commons.common import get_png
from commons.logs import Logging

logger = Logging()


class PCWaitElement(WaitElement):

    def __init__(self, driver):
        self.driver = driver

    def display_id(self, *args, **kwargs):  # id显示等待
        """
        每0.5秒轮寻一次属性id为element的元素是否可见，可见就跳出等待，返回等等元素出现成功；超过seconds秒便等待失败，返回元素等待出现失败
        :param args:
        :param kwargs:
        :return:
        """
        try:
            element = kwargs['element']
        except KeyError:
            logger.err().error('未传需要等待元素的定位参数')
            return False

        try:
            seconds = kwargs['seconds']
            if seconds is None:
                seconds = 10
        except KeyError:
            seconds = 10

        try:
            WebDriverWait(self.driver, seconds, 0.5).until(EC.visibility_of_element_located((By.ID, element)))
        except TimeoutException:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址: %s \n' % screen)
            raise TimeoutException('元素不存在，定位失败')

        return True

    def display_name(self, *args, **kwargs):  # name显示等待
        """
        每0.5秒轮寻一次属性name为element的元素是否可见，可见就跳出等待，返回等等元素出现成功；超过seconds秒便等待失败，返回元素等待出现失败
        :param args:
        :param kwargs:
        :return:
        """
        try:
            element = kwargs['element']
        except KeyError:
            logger.err().error('未传需要等待元素的定位参数')
            return False

        try:
            seconds = kwargs['seconds']
            if seconds is None:
                seconds = 30
        except KeyError:
            seconds = 30

        try:
            WebDriverWait(self.driver, seconds, 0.5).until(EC.visibility_of_element_located((By.NAME, element)))
        except TimeoutException:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址: %s \n' % screen)
            raise TimeoutException('元素不存在，定位失败')

        return True

    def display_class(self, *args, **kwargs):  # class显示等待
        """
        每0.5秒轮寻一次属性class为element的元素是否可见，可见就跳出等待，返回等等元素出现成功；超过seconds秒便等待失败，返回元素等待出现失败
        :param args:
        :param kwargs:
        :return:
        """
        try:
            element = kwargs['element']
        except KeyError:
            logger.err().error('未传需要等待元素的定位参数')
            return False

        try:
            seconds = kwargs['seconds']
            if seconds is None:
                seconds = 30
        except KeyError:
            seconds = 30

        try:
            WebDriverWait(self.driver, seconds, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, element)))
        except TimeoutException:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址: %s \n' % screen)
            raise TimeoutException('元素不存在，定位失败')

        return True

    def display_xpath(self, *args, **kwargs):  # xpath显示等待
        """
        每0.5秒轮寻一次属性xpath为element的元素是否可见，可见就跳出等待，返回等等元素出现成功；超过seconds秒便等待失败，返回元素等待出现失败
        :param args:
        :param kwargs:
        :return:
        """
        try:
            element = kwargs['element']
        except KeyError:
            logger.err().error('未传需要等待元素的定位参数')
            return False

        try:
            seconds = kwargs['seconds']
            if seconds is None:
                seconds = 30
        except KeyError:
            seconds = 30

        try:
            WebDriverWait(self.driver, seconds, 0.5).until(EC.visibility_of_element_located((By.XPATH, element)))
        except TimeoutException:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址: %s \n' % screen)
            raise TimeoutException('元素不存在，定位失败')

        return True

    def display_css(self, *args, **kwargs):  # css显示等待
        """
        每0.5秒轮寻一次属性css为element的元素是否可见，可见就跳出等待，返回等等元素出现成功；超过seconds秒便等待失败，返回元素等待出现失败
        :param args:
        :param kwargs:
        :return:
        """
        try:
            element = kwargs['element']
        except KeyError:
            logger.err().error('未传需要等待元素的定位参数')
            return False

        try:
            seconds = kwargs['seconds']
            if seconds is None:
                seconds = 30
        except KeyError:
            seconds = 30

        try:
            WebDriverWait(self.driver, seconds, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
        except TimeoutException:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址: %s \n' % screen)
            raise TimeoutException('元素不存在，定位失败')

        return True

    def hide_wait_element(self, *args, **kwargs):  # 隐式等待
        """
        等待seconds秒成功返回 True
        :param args:
        :param kwargs:
        :return:
        """
        try:
            seconds = kwargs['seconds']
        except KeyError:
            seconds = 10
        try:
            self.driver.implicitly_wait(seconds)
        except NoSuchElementException:
            screen = get_png(self.driver)
            logger.err().error('\n错误截图地址: %s \n' % screen)
            raise NoSuchElementException('元素不存在，定位失败')

        return True
