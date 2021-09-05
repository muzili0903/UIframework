"""
@Time ： 2021/7/6 21:33
@Auth ： muzili
@File ： browserOperator.py
@IDE  ： PyCharm
"""
import os
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from commons.getConfig import Config
from commons.getFileDirs import BROWSERDRIVER
from commons.logs import Logging

logger = Logging()


class BrowserOperator(object):

    def __init__(self):
        self.conf = Config()
        self.driver_path = os.path.join(BROWSERDRIVER, 'chromedriver.exe')
        self.driver_type = str(self.conf.get_config('base', 'browser_type')).lower()
        self.url = self.conf.get_config('base', 'url')
        self.driver = None

    def open_url(self):
        """
        打开网页
        :return:
        """
        if self.url is None:
            return '没有url'

        try:
            if self.driver_type == 'chrome':
                self.driver = webdriver.Chrome(executable_path=self.driver_path)
                self.driver.maximize_window()
                self.driver.get(self.url)
            elif self.driver_type == 'ie':
                self.driver = webdriver.Ie(executable_path=self.driver_path)
                self.driver.maximize_window()
                self.driver.get(self.url)
            elif self.driver_type == 'firefox':
                self.driver = webdriver.Firefox(executable_path=self.driver_path)
                self.driver.maximize_window()
                self.driver.get(self.url)
            else:
                logger.err().error("没有该浏览器：", self.driver_type)
                raise KeyError("没有该浏览器")
        except Exception as e:
            logger.err().error(e)
            raise KeyError("驱动文件路径错误")
        return self.driver

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        time.sleep(3)
        self.driver.close()
        return True

    def quit_browser(self):
        """
        退出浏览器
        :return:
        """
        time.sleep(3)
        self.driver.quit()
        return True

    def back(self):
        """
        后退
        :return:
        """
        self.driver.back()
        return True

    def forward(self):
        """
        前进
        :return:
        """
        self.driver.forward()
        return True

    def delete_cookie(self, cookie):
        """
        删除指定的cookie
        :param cookie:
        :return:
        """
        self.driver.delete_cookie(cookie)
        return True

    def delete_all_cookies(self):
        """
        删除所有的cookies
        :return:
        """
        self.driver.delete_all_cookies()
        return True

    def get_cookie(self, cookie):
        """
        获取指定的cookie
        :param cookie:
        :return:
        """
        return self.driver.get_cookie(cookie)

    def get_cookies(self):
        """
        获取所有的cookies
        :return:
        """
        return self.driver.get_cookies()

    def execute_script(self, script):
        """
        执行js脚本
        :param script:
        :return:
        """
        self.driver.execute_script(script)

    def get_wind_position(self, wind='current'):
        """
        获取当前窗口的x,y位置
        :return: 返回一个字典 {'x': 9, 'x': 9}
        """
        return self.driver.get_window_position(windowHandle=wind)

    def set_wind_position(self, x, y, wind='current'):
        """
        给页面设置x,y位置
        :param x:
        :param y:
        :param wind:
        :return:
        """
        if type(x) is not int or type(y) is not int:
            logger.err().error('x or y is not int type')
            return False
        try:
            self.driver.set_window_position(x, y, windowHandle=wind)
        except Exception as e:
            logger.err().error(e)
            logger.err().error('传入错误的窗口句柄')
            return False
        return True

    def get_window_size(self, wind='current'):
        """
        获取当前窗口的宽高(width,height)
        :param wind:
        :return: 返回一个字典 {'width': 1051, 'height': 806}
        """
        return self.driver.get_window_size(windowHandle=wind)

    def set_window_size(self, width, height, wind='current'):
        """
        给页面设置宽高
        :param width:
        :param height:
        :param wind:
        :return:
        """
        if type(width) is not int or type(height) is not int:
            logger.err().error('width or height is not int type')
            return False
        try:
            self.driver.set_window_size(width, height, windowHandle=wind)
        except Exception as e:
            logger.err().error(e)
            logger.err().error('传入错误的窗口句柄')
            return False
        return True

    def refresh(self):
        """
        刷新
        :return:
        """
        self.driver.refresh()

    def set_page_load_timeout(self, **kwargs):
        """
        给载入页面设置一个超时时间
        :return:
        """
        try:
            url = kwargs['url']
        except KeyError:
            logger.err().error('没有URL参数')
            return False

        try:
            seconds = kwargs['seconds']
        except KeyError:
            seconds = 10

        try:
            self.driver.get(url)
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        self.driver.set_page_load_timeout(seconds)

    def get_current_url(self):
        """
        获取当前url
        :return:
        """
        return self.driver.current_url()


if __name__ == "__main__":
    browser = BrowserOperator()
    driver = browser.open_url()
