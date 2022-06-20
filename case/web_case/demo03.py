# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/13 3:54 PM 
# ide： PyCharm
import logging

import pytest

from api_keyword.base_word import KeyWord
from case_data.data_driver.yaml_driver import Read_Data
from log.logger_config import test2_log

A=Read_Data()
log=test2_log()
@pytest.mark.parametrize(('account,pwd,msg'),[['admin','123456','success'],['wwg','123456','success']],ids=['case1','case2'])
# @pytest.mark.parametrize(('url,account,pwd'),A.read_yaml()['ids'],ids=A.read_yaml()['data'])

def test_get_token(account,pwd,msg):
    ak = KeyWord()
    # url = 'http://39.98.138.157:5000/api/login'
    url='http://39.98.138.157:5000/api/login'
    data = {
        "username": account,
        "password": pwd
         }
    hd = {'Content-Type': 'application/json'}
    res=ak.post(url=url,data=data,headers=hd)
    print('测试')
    # print(res.text)
    assert res.json()['msg'] == msg, '登录成功'
    # log.info('错误信息')
    # token=res.json()['token']

    # log.info('错误信息')

    # log.info('{}---{}'.format(A.get_yaml()['data'],A.get_yaml()['ids']))
if __name__ == '__main__':
    pytest.main(['-s','demo06.py'])