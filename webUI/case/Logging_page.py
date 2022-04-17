# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/14 12:22 PM 
# ide： PyCharm
import time
import unittest

from ddt import ddt, data, file_data, unpack
from selenium import webdriver

from webUI.case.buy_page import Buy_Page
from webUI.case.log_page import Loggin_Page

from webUI.keyword.common import Common
from webUI.web_log.weblog_config import web_log
# chromeOptions = webdriver.ChromeOptions()
# cls.driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument(
#     r'--user-data-dir=/Users/kevin.wu/Library/Application Support/Google/Chrome/Default'))


@ddt
class Test_Login(unittest.TestCase):

    @classmethod
    # 静态方法，支持调用类属性，不可以直接访问实例
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.lp = Loggin_Page(cls.driver)
        cls.bp = Buy_Page(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.bp.quit()



    @data(['wwg', '123456'])
    @unpack
    def test_01(self, user, pwd):
        self.lp.login(user, pwd)


    @file_data('../data/data1.yaml')
    def test_02(self, txt):
        self.bp.search(txt)


if __name__ == '__main__':
    unittest.main()

# 打开浏览器

# 定位登录页面


# 输入账户密码，点击登录


# 登录成功，校验登录是否成功
