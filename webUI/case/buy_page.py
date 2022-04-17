# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/15 4:04 PM 
# ide： PyCharm
from ddt import ddt, file_data
from selenium import webdriver

from webUI.keyword.common import Common


class Buy_Page(Common):

    # 便于管理，环境管理和按钮管理，方便之后前端开发有改动的时候能够快速维护现有的自动化测试框架
    url='http://39.98.138.157/shopxo/'
    search_inpout=('name','wd')
    search_button=('id','ai-topsearch')

    # 搜索页面操作
    # @file_data('../data/data1.yaml')
    def search(self,txt):
        self.open(self.url)
        self.max_browser()
        self.input(*self.search_inpout,txt)
        self.click(*self.search_button)
        # self.quit()

if __name__ == '__main__':
    bp=Buy_Page('Chrome')
    bp.search('手机')

