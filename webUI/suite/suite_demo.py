# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/17 12:08 PM 
# ide： PyCharm

'''

skip装饰器
unittest.skip
unittest.skipif(condition=,reason='')
unittest.skipunless()

套件：suite  运行器：runner

suite=unittest.suite()

runner=unittest.TextTestRunner()

测试报告模块应用,常用的报告模块文件，无需通过pip模式安装，下载py文件，安装在lib文件夹中
HTMLTestRunner
'''



import os
import unittest

from webUI.case.log_page import Loggin_Page

suite=unittest.TestSuite()


# 添加自己想要运行的测试用例
# suite.addTest(Loggin_Page())
#
# # 添加单条测试用例
# suite.addTest(Loggin_Page())
# 添加多条测试用例，基于list的形式去添加多条测试用例
# cases=[class(test01),class(test02)]
# suite.addTest(cases)

# 添加一整个class进入套件,Test_Class属于 测试类名称
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Class))

# 通过文件名添加进入测试


# suite.addTests(unittest.TestLoader().loadTestsFromName('py文件.py文件中的类'))

# 批量添加：持续集成，批量管理中比较好用
# 定义用例的获取路径,测试用例的路径

'''************************************'''
path='../case'
discover=unittest.defaultTestLoader.discover(start_dir=path,pattern='*page.py')
runner=unittest.TextTestRunner(verbosity=2)
runner.run(discover)

# runner.run(suite)
# verbosity:0-1-2：日志等级
'''************************************'''
# 默认返回一个套件对象
"""
路径
主题
描述
"""
# report_dir=''
# report_title=''
# report_description=''
#
# #生成路径
# if os.path.exists(report_dir):
#     os.mkdir(report_dir)

# 生成htmltestrunner测试报告，本质上是写入一个py文件
# HTMLTestRunnerCN

# 报告发送邮件
# report_file=report_dir+'report.html'
#
#
#
#
# with open(report_file,'wb',) as file:
#     runner= HTMLTestRunner
#     runner.run(discover)


