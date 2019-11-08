"""
@description: 提供一些工具函数
@author: Cui Rui long
@email: xiaocuikindle@163.com
@time: 2019-11-08
@version: 0.0.1
"""


def is_chinese(uchar):
    """
    判断一个unicode是否是汉字
    :param uchar:
    :return:
    """
    if (uchar >= u'\u4e00') and (uchar <= u'\u9fa5'):
        return True
    else:
        return False
