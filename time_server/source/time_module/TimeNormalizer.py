"""
@description: 日期、时间归一化类
@author: Cui Rui long
@email: xiaocuikindle@163.com
@time: 2019-11-08
@version: 0.0.1
"""
import regex
import json
import re
import arrow
import yaml
import logging

logger = logging.getLogger("server_log")


class TimeNormalizer(object):
    def __init__(self):
        self.pattern = None

    def test(self):
        pass
