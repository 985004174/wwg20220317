# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/12 9:52 AM 
# ide： PyCharm
import json
from urllib import request

import pytest
import requests

from api_keyword.base_word import KeyWord


# url='http://39.98.138.157:5000/api/login'
# data={
# "password": "123456",
# "username": "admin"
# }
# hd = {'Content-Type': 'application/json'}
# res1=requests.post(url,json=data,headers=hd)
# print(res1.json()['token'])

@pytest.fixture(scope='function')
# @pytest.mark.parametrize('url,account,pwd',('http://39.98.138.157:5000/api/login','admin','123456'),ids='case1')
def get_token():
    ak = KeyWord()
    url = 'http://39.98.138.157:5000/api/login'
    data = {
        "username": 'admin',
        "password": '123456'
         }
    hd = {'Content-Type': 'application/json'}
    res=ak.post(url=url,data=data,headers=hd)
    token=res.json()['token']
    print(token)

    return token,res

if __name__ == '__main__':
    get_token()
