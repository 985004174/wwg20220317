# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/15 2:19 PM 
# ide： PyCharm
from selenium import webdriver

from webUI.keyword.common import Common

# 页面对象
class Loggin_Page(Common):

    # 便于管理
    url='http://39.98.138.157/shopxo/'
    account=('name','accounts')
    passwrod=('name','pwd')
    button1=('xpath','/html/body/div[6]/div/div[1]/div[2]/a[1]')
    button2=('xpath','//button[text()="登录"]')


    def login(self,accounts,pwd):
        self.open(self.url)
        self.max_browser()
        self.click(*self.button1)
        self.input(*self.account,accounts)
        self.input(*self.passwrod,pwd)
        self.click(*self.button2)
        # self.quit()




if __name__ == '__main__':
    # driver=webdriver.Chrome()
    lp=Loggin_Page('Chrome')
    lp.login('wwg','123456')


