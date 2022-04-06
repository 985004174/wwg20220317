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

from config.url_config import URL_ADMIN

@allure.epic('LLP系统')
@allure.feature('登录模块')
class Test_Control:
    @allure.story('01.登录获取token')
    @allure.severity('critical')
    def test_getUserInfo(self,token_admin):
        ak, token = token_admin
        url = URL_ADMIN + 'getUserInfo'
        hd = {'token': token}
        res1 = ak.get(url, headers=hd)
        print(res1.text)
        token1 = ak.get_text(res1.text,'token')
        print(token1)
        return token1,ak


    @allure.feature('后台首页数据看板')
    @allure.story('02.获取经销商信息下拉列表')
    @allure.severity('critical')
    # @pytest.mark.slow
    def test_agent_selectList(self,token_admin):
        """
        获取经销商信息下拉列表
        """
        ak, token = token_admin
        url = URL_ADMIN+'agent/selectList'
        hd = {'token': token}
        res2 = ak.get(url,headers=hd)
        print(res2.text)
        ret = res2.json()['ret']
        assert ret == 0
        print('接口正常')

    @allure.story('03.数据面板数据接口测试')
    @allure.severity('blocker')
    def test_statistics(self,token_admin):
        """
        获取数据面板测试数据
        """
        ak, token = token_admin
        url = URL_ADMIN + 'console/dataBriefing'
        hd = {'token': token}
        data={"dateType":"curYea","startTime":1640966400000,"endTime":1648553722536}
        res3= ak.post(url,headers=hd,data=data)
        ret = res3.json()['ret']
        assert ret == 0











if __name__ == '__main__':
    # pytest.main(['-s', 'test_demo01.py'])
    pytest.main(['test_demo01.py','--alluredir','./allure_report','--allure-severities','blocker,critical','--clean-alluredir'])
    os.system('allure generate ./allure_report -o ./report/ --clean')
