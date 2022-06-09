# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/5/31 10:31 AM 
# ide： PyCharm
import allure
import pytest

from Api_keywords.api_key import Http_Request_Control, ApiKey
from Api_keywords.yaml_read import Ymal_Control


@allure.epic('测试1')
class Test_01:
    # 获取用户信息
    file = '../yaml_Case/test1.yaml'
    yaml_data = Ymal_Control().read_yaml(filepath=file)

    @pytest.mark.parametrize('data', yaml_data)
    def test_1(self, data):
        res = Http_Request_Control().http_request(data)
        allure.dynamic.title(data['title'])
        userid = ApiKey().get_text(res.text, 'userid')
        openid = ApiKey().get_text(res.text, 'openid')
        # print(res.json()['httpstatus'])

        # print(data['case_id'])
        assert res.json()['httpstatus'] == data['status'], '测试通过'
        return userid, openid

    # 获取商品信息
    # file = '../yaml_Case/test2.yaml'
    # yaml_data = Ymal_Control().read_yaml(filepath=file)
    #
    # @pytest.mark.parametrize('data', yaml_data)
    # def test_2(self, data):
    #     res = Http_Request_Control().http_request(data)
    #     print(res.text)
    #
    # # 添加购物车
    # file = '../yaml_Case/test2.yaml'
    # yaml_data = Ymal_Control().read_yaml(filepath=file)
    #
    # @pytest.mark.parametrize('data', yaml_data)
    # def test_3(self, data):
    #     res = Http_Request_Control().http_request(data)
    #     print(res.text)
    #
    #
    #
    # # 获取用户信息
    # file = '../yaml_Case/test3.yaml'
    # yaml_data = Ymal_Control().read_yaml(filepath=file)
    #
    # @pytest.mark.parametrize('data', yaml_data)
    # def test_4(self, data):
    #     res = Http_Request_Control().http_request(data)
    #     print(res.text)
    #



if __name__ == '__main__':
    pytest.main(['-s'])
