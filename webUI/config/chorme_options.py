# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/16 3:35 PM 
# ide： PyCharm
import time

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')


driver=webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')
time.sleep(3)

#去掉警告

# 去掉Chrome提示受到自动软件控制,已经弃用
# options.add_argument('disable-infobars')


