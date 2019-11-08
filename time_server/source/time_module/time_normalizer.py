"""
@description: 日期、时间归一化类
@author: Cui Rui long
@email: xiaocuikindle@163.com
@time: 2019-11-08
@version: 0.0.1
"""
import regex
import json
import arrow
import yaml
import logging
from pprint import pprint
from time_server.source.time_module.app_info import AppInfo
from time_server.source.time_module.utils import *

logger = logging.getLogger("server_log")


class TimeNormalizer(object):
    def __init__(self):
        self.app_info = AppInfo()
        self.pattern = regex.compile(self.app_info.get_pattern())

    def init(self):
        pass

    def __pre_process(self, sentence):
        """
        数据预处理：清理句中的空格、汉字转数字
        :param sentence:
        :return:
        """
        sentence = delete_word_rule(sentence, u"\\s+")  # 清理空白字符
        sentence = translate_number(sentence)  # 汉字转数字
        return sentence

    def time_pattern_candidate(self, sentence):
        start_line = -1
        end_line = -1
        num = 0
        temp = []
        match = self.pattern.finditer(sentence)
        pprint("===============")
        pprint("用正则提取关键字：")
        for m in match:
            pprint(m)
            start_line = m.start()
            if start_line == end_line:
                num -= 1
                temp[num] = temp[num] + m.group()
            else:
                temp.append(m.group())
            end_line = m.end()
            num += 1
        pprint(temp)
        pprint("===============")

    def parse(self, sentence):
        """
        日期归一化函数
        :param sentence:
        :return:
        """
        sentence = self.__pre_process(sentence)
        self.time_pattern_candidate(sentence)
        return {"sen": sentence}
