# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/3/29 7:37 PM 
# ide： PyCharm
import pytest
import requests

@pytest.fixture(scope='session',autouse=True)
def get_token():
    data={
        "password": "123456",
        "username": "admin"
        }
    url='http://39.98.138.157:5000/api/login'
    method='post'
    res=requests.request(url=url,method=method,json=data)

    token=res.json()['token']
    print(token)
    return token


if __name__ == '__main__':
    get_token()