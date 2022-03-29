# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/3/29 10:11 AM 
# ide： PyCharm
import json

import jsonpath
import requests


# r = requests.get(url='url', params=None)
# p = requests.post(url='url', json='data')


class ApiKey:
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    def post(self, url, data=None, **kwargs):
        return requests.post(url, data=data, **kwargs)

    def get_text(self, data, key):
        dict_data = json.loads(data)
        # 数据源转换json，loads讲json格式内容转换为字典格式
        value = jsonpath.jsonpath(dict_data, '$..{0}'.format(key))
        # print(value)
        # jsonpath返回list，失败返回false，
        # 根目录下面的任意键,jsonpath还需要学习
        return value[0]
