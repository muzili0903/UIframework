"""
@Time ： 2021/8/30 20:54
@Auth ： muzili
@File ： logs.py
@IDE  ： PyCharm
"""
from commons.getConfig import Config
from commons.getFileDirs import LOGS
import logging


class Logging(object):

    def __init__(self):
        self.conf = Config()
        self.LOGS = LOGS
        self.logger = None
        self.DEBUG = eval(self.conf.get_config('log', 'debug').capitalize())

    def _logs(self, file, level, formatter):
        self.logger = logging.getLogger(str(level))
        self.logger.setLevel(level=level)
        handler = logging.FileHandler(file)
        formatter = logging.Formatter(formatter)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        if self.DEBUG is not False:
            console = logging.StreamHandler()
            console.setLevel(level=level)
            console.setFormatter(formatter)
            self.logger.addHandler(console)

    def info(self):
        logs = self.LOGS + '\\log'
        formatter = '%(asctime)s - %(pathname)s - %(levelname)s - %(message)s'
        self._logs(file=logs, level=logging.INFO, formatter=formatter)
        return self.logger

    def err(self):
        logs = self.LOGS + '\\errs'
        formatter = '%(asctime)s %(levelname)s [%(process)d-%(threadName)s] %(pathname)s %(module)s.%(funcName)s line %(lineno)d: %(message)s'
        self._logs(file=logs, level=logging.ERROR, formatter=formatter)
        return self.logger

    def get_logger(self)
        return self.logger


log = Logging()
logger = log.get_logger()

if __name__ == '__main__':
    pass
