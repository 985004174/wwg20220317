# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/12 2:15 PM 
# ide： PyCharm
import json
import logging

import pytest

from api_keyword.base_word import KeyWord
from config.enviroment import URL
from log.logger_config import test2_log



class Test_Order():
    '''
    新增定车订单
    '''

    def test_add_Dorder(self, get_token):

        token, ak = get_token
        hd = {'Content-Type':'application/json','token': token}
        url = URL+'url'
        data = '{"count": 2, "paytype": 1, "price": 100}'
        res = ak.post(url=url, headers=hd, json=data)
        res_price=(res.json()['data']['price'])
        print(res_price)




if __name__ == '__main__':
    pytest.main(['-s', 'create_order.py'])
