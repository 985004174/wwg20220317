# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/3/29 2:30 PM 
# ide： PyCharm
import json
import os

import allure
import pytest
import requests


from Api_keywords.api_key import ApiKey

from config.url_config import URL

@allure.epic('获取用户信息接口')
class Test_Control:
    @allure.story('01.登录获取token')
    def test_getUserInfo(self,token_fix):
        ak, token = token_fix
        url = URL + 'getUserInfo'
        hd = {'token': token}
        res1 = ak.get(url, headers=hd)
        print(res1.text)
        token1 = ak.get_text(res1.text,'token')
        print(token1)
        return token1,ak


    @allure.story('02.获取经销商信息下拉列表')
    def test_agent_selectList(self,token_fix):
        ak, token = token_fix
        url = URL+'agent/selectList'
        hd = {'token': token}
        res2 = ak.get(url,headers=hd)
        print(res2.text)
        ret = res2.json()['ret']
        assert ret == 0
        print('接口正常')

    @allure.story('03.数据面板数据接口测试')
    def test_statistics(self,token_fix):
        ak, token = token_fix
        url = URL + 'console/dataBriefing'
        hd = {'token': token}
        data={"dateType":"curYea","startTime":1640966400000,"endTime":1648553722536}
        res3= ak.post(url,headers=hd,data=data)
        ret = res3.json()['ret']
        if ret == 500:
            print('接口异常')
        else:
            print('接口正常')







if __name__ == '__main__':
    # pytest.main(['-s', 'test_demo01.py'])
    pytest.main(['test_demo01.py','--alluredir','./allure_report','--clean-alluredir'])
    os.system('allure generate ./allure_report -o ./report/ --clean')
