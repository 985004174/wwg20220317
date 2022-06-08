# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/3/29 10:11 AM 
# ide： PyCharm
import enum
import json
import os.path
from enum import Enum

import allure
import jsonpath
import numpy
import pytest
import requests


# r = requests.get(url='url', params=None)
# p = requests.post(url='url', json='data')
import yaml
from yaml import FullLoader

from Api_keywords.yaml_read import Ymal_Control


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



class YamlData(Enum):

    HOST='host'
    URL='url'
    METHOD='method'
    DATA='data'
    STATUS='status'


class Http_Request_Control:

    def http_request(self,data, **kwargs):
        '''

        :param data: yaml_data
        :return:
        '''


        URL=data['data']['url']
        METHOD=data['data']['method']
        PARAMAS=data['data']['paramas']
        STATUS=data['data']['status']
        CODE=data['data']['code']
        HEADERS=data['data']['headers']



        res=requests.request(url=URL,method=METHOD,json=PARAMAS,headers=HEADERS,**kwargs)
        print(res.text)
        return res



# if __name__ == '__main__':
#     # filepath='../case/yaml_Case/test1.yaml'
#     # Ymal_Control().read_yaml(filepath=filepath)
#
#     data=Ymal_Control().read_yaml(filepath='../case/yaml_Case/test1.yaml')
#     Http_Request_Control().http_request(data)

