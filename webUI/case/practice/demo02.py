# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/14 5:06 PM 
# ide： PyCharm
import time

import cosmos as cosmos

# c1={name:'_hll_identifier_stg',value:'rIf+lXRMubkSVa84+MBsfAeJ9P1SamKenkgSHz3AgKSQKSyLKkXrajfSxLEXIDeLS3pgLr7oAyadGdxKb3VPL2wVHMFJxqKoxQNByV0vfZ7+6Ic34WeamcDDU0siUCKb5ImWCAGRQ9LfgrBJVyB/Kl3kqQaiSGI50qYD/ej7b5k='}
from selenium import webdriver
from selenium.webdriver import ActionChains


class AC():
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://www.baidu.com')

    def Action_Chain(self, name, value, txt):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        self.driver.find_element(name, value).send_keys(txt)
        # 定位到需要悬停的元素
        # el = self.driver.find_element(name, value)
        # 悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element(name, value)).perform()
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    A=AC()
    A.Action_Chain('name','wd','测试')
