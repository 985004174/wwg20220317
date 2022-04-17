# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/14 12:20 PM 
# ide： PyCharm
import time

from selenium import webdriver


def open_browser(type_):
    if type_ == 'Chrome':
        driver = webdriver.Chrome()
        time.sleep(6)
        # print(type(driver))
    else:
        try:
            driver = getattr(webdriver, type_)()
        #     driver = webdriver.type_()
        except Exception as e:
            print('异常信息：{}'.format(e))
            driver = webdriver.Chrome()
    return driver

if __name__ == '__main__':
    open_browser('Chrome')