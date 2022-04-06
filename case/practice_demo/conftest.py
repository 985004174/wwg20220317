# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/4 3:59 PM 
# ide： PyCharm
import json

import jsonpath
import pytest

from Api_keywords.api_key import ApiKey
URL='http://39.98.138.157:5000/'
@pytest.fixture(scope='session')
def get_token():
    ak = ApiKey()
    url=URL+'api/login'
    data={
      "password": "123456",
      "username": "admin"
    }

    hd={'Content-Type': 'application/json'}
    res = ak.post(url=url,json=data,headers=hd)
    token = res.json()['token']
    print(token)
    return ak,res,token

token='23657DGYUSGD126731638712GE18271H'