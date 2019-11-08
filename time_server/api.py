"""
@description: Django 服务入口文件，提供 get_result 接口返回查询图
@author: Cui Rui long
@email: xiaocuikindle@163.com
@time: 2019-11-08
@version: 0.0.1
"""
import timeit
import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from time_server.source.time_module.time_normalizer import TimeNormalizer

# 定义整体服务用到的日志文件
logger = logging.getLogger("server_log")


# 在这里定义在整个程序都会用到的类的实例
time_normalizer = TimeNormalizer()


# 服务的接口文档
@csrf_exempt
def get_result(request):
    """
    input: 接收客户端发送的POST请求：{"sentence": "raw_sentence"}
    output: 服务器返回JSON格式的数据，返回的数据格式如下：
    :param request: 用户输入的查询句子
    :return
    """

    if request.method != 'POST':
        logger.error("仅支持post访问")
        return JsonResponse({"result": {}, "msg": "仅支持post访问"}, json_dumps_params={'ensure_ascii': False})

    request_data = json.loads(request.body)
    sentence = request_data['sentence']

    start_time = timeit.default_timer()

    # 时间归一化逻辑代码
    result = time_normalizer.parse(sentence)

    end_time = timeit.default_timer()
    logger.info("Full time consume: {0} S.\n".format(end_time - start_time))
    # 返回JSON格式数据，将 result_ner 替换成需要返回的JSON数据
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})