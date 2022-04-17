# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/16 2:53 PM 
# ide： PyCharm
# import locust
# import pytest
# import requests
#
# class Test_Case(locust.HttpUser):
#     # 指定time属性
#     wait_time = locust.between(1, 2)
#     # 每个task间隔1。2秒左右，每个用例在执行的时候会有间隔差，每个请求间隔task1-2秒
#
#     @locust.task
#     def test_01(self,url):
#         res=requests.get(url)
#         # res=self.client.get('url')
#         assert res.status_code==200
#
# if __name__ == '__main__':
#     # url='https://www.baidu.com'
#     # A=Test_Case()
#     # A.test_01(url)


# 多线程和分布式
# 多线程模块：threading