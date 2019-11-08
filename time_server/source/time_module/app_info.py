"""
@description: 系统配置信息
@author: Cui Rui long
@email: xiaocuikindle@163.com
@time: 2019-11-08
@version: 0.0.1
"""

import os
import json


class AppInfo(object):
    """
    系统内部配置信息
    """
    # status 字段编码
    # 20X 标识的是服务器正常工作情况下可能返回的字段
    OK = '200'  # 无任何异常情况

    _instance = None  # 单例模式-用来存放实例

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        root_path = str(os.getcwd()).replace("\\", "/")
        if 'source' in root_path.split('/'):
            self.base_path = os.path.join(os.path.pardir, os.path.pardir)
        else:
            self.base_path = os.getcwd()

        self.pattern_path = os.path.join(self.base_path, "data")
        self.pattern_file = "pattern.txt"
        self.pattern = None

    def get_pattern(self):
        if self.pattern is not None:
            return self.pattern
        else:
            if not os.path.exists(os.path.join(self.pattern_path, self.pattern_file)):
                print("The pattern file is not exists.")

            with open(os.path.join(self.pattern_path, self.pattern_file), 'r', encoding='utf-8') as f_r:
                self.pattern = f_r.read()
                return self.pattern
