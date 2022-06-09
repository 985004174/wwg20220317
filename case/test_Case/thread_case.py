# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/6/9 4:44 PM 
# ide： PyCharm
import threading




def task(nums):
    num = 0
    for i in range(10000000):
        num += 1
    print(num)


t = threading.Thread(target=task,args=(5,))
t.start()



# 利用Thread创建线程，target参数接收函数名，args参数接收函数的参数，start方法启动线程