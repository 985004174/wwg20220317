# -- coding: utf-8 --
# @time :
# @author : 吴文光
# @email :985004174@qq.com
# @file : .py
# @software: pycharm
import json
import os

import allure
import jsonpath
import pytest
import requests

from Api_keywords.api_key import ApiKey


from Api_keywords.yaml_read import Ymal_Control


from datetime import datetime
@allure.epic('用户信息模块')
class Test_Case:


    def test1(self, get_token):
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        hd = {'token': get_token}
        res1 = ApiKey().get(url=url, headers=hd)
        print(res1.text)
        openid=ApiKey().get_text(res1.text, 'openid')
        return res1

    # 添加商品至购物车
    def test2(self,get_token):
        with allure.step('从个人信息接口获取相关openid，userid'):
            res1=self.test1(get_token)
        with allure.step('发送添加商品请求至购物车'):
            url='http://39.98.138.157:5000/api/addcart'
            hd={'token':get_token}
            data={
                'openid':ApiKey().get_text(res1.text,'openid'),
                'userid':ApiKey().get_text(res1.text,'userid'),
                'productid': 8888
            }
            res2=ApiKey().post(url=url,headers=hd,json=data)
            print(res2.text)
        with allure.step('接口返回信息校验'):
            print(datetime.now())
            print('自动化构建测试')
            result=ApiKey().get_text(res2.text,'result')
            assert 'success' == result


# if __name__ == '__main__':
#     # pytest.main(['-vs', 'test_1.py'])
#     pytest.main(['test_1.py','--alluredir','../report/report','--clean-alluredir'])
#     os.system('allure generate ../report/report -o ./allure-report --clean')
#     # os.system('allure server ../report')
