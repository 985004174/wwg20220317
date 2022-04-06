# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/4 3:57 PM 
# ide： PyCharm
'''
用例：登录模块
'''
import os

import allure
import pytest

from case.practice_demo.conftest import URL


@allure.epic('登录模块')
class Test_Loggin():
    # @allure.feature('测试获取个人信息接口')
    @allure.story('01.基于token获取个人信息接口')
    @allure.testcase('www.baidu.com')
    @allure.issue('www.baidu.com')
    def test_login(self,get_token):
        ak,res,token = get_token
        url = URL+'api/getuserinfo'
        hd={'token':token}
        res1=ak.get(url=url,headers=hd)
        print(res1.text)
        user_id=res1.json()['data'][0]['userid']
        user_id2=ak.get_text(res1.text,'userid')

        print(user_id,user_id2)
        assert user_id==17890

    @allure.story('02.获取商品信息接口')
    def test_getgodsinfo(self,get_token):
        pass








if __name__ == '__main__':
    pytest.main(['-s','demo01.py','--alluredir','./kevin','--clean-alluredir'])
    os.system('allure generate ./kevin -o ../report/api_report --clean')
