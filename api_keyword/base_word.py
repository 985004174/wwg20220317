# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/11 7:30 PM 
# ide： PyCharm
import json

import jsonpath
import requests


class KeyWord:
    def get(self,url,data=None,**kwargs):
        return requests.get(url,json=data,**kwargs)

    def post(self,url,data,**kwargs):
        return requests.post(url,json=data,**kwargs)

    def get_text(self, data, key):
        """
        :param data: 响应文本
        :param key: key值
        :return:
        """

        dict_data = json.loads(data)
        # 数据源转换json，loads讲json格式内容转换为字典格式
        value = jsonpath.jsonpath(dict_data, '$..{0}'.format(key))
        # print(value)
        # jsonpath返回list，失败返回false，
        # 根目录下面的任意键,jsonpath还需要学习
        return value[0]
