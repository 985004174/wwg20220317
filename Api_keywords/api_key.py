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


    # 匹配过滤
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


# class Denpendence_test:
#     def denpendency_01(self):
#         if


class Http_Request_Control:

    def http_request(self,data, **kwargs):
        '''

        :param data: yaml_data
        :return:
        '''


        URL=data['url']
        METHOD=data['method']
        PARAMAS=data['paramas']
        STATUS=data['status']
        CODE=data['code']
        HEADERS=data['headers']
        Dependence=data['Dependence']
        Dependence_case=data['dependence_case']


        if Dependence is False or Dependence_case is None:
            res=requests.request(url=URL,method=METHOD,json=PARAMAS,headers=HEADERS,**kwargs)
            return res
        # 获取依赖的用例case
        else:
            a=data['dependence_case']
            print(a)
            return a,


          # res=requests.request(url=URL,method=METHOD,json=PARAMAS,headers=HEADERS,**kwargs)









# if __name__ == '__main__':
#     # filepath='../case/yaml_Case/test1.yaml'
#     # Ymal_Control().read_yaml(filepath=filepath)
#
#     data=Ymal_Control().read_yaml(filepath='../case/yaml_Case/test1.yaml')
#     Http_Request_Control().http_request(data)

