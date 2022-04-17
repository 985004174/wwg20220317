# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/13 11:05 AM 
# ide： PyCharm
import yaml
import pytest
import logging

# 被测对象
# def add(a, b):
#     return a + b
#
# def get_yaml():
#     # 打开一个文件，生成文件流对象
#     with open('../c') as f:
#         # 使用yaml解析文件流，生成一个Python可识别的数据类型
#         data = yaml.load(f)
#         print(data)
#     return data
#
# def test_get_yaml():
#     get_yaml()
#
# # 测试脚本
# class TestAdd:
#
#     def setup_class(self):
#         pass
#
#     def teardown_class(self):
#         pass
#
#     @pytest.mark.add
#     @pytest.mark.parametrize("a, b,expect",get_yaml()["data"],ids=get_yaml()["ids"])
#
#     def test_add(self, a, b, expect):
#         assert expect == add(a, b)

# str_1_data = ' a b c '
# str_2_list = str_1_data.split()
# print(str_2_list)

list1 = [1, 3, 2, 4, 5, 77, 63, 22]
list1.sort()
print(list1)
str="a b c "
# str.split(' ')
# print(type(str))
str.replace(" ",'-',2)
print(str)
# 返回none


list1=[6,2,3,4,5,3,9,30,133,111]
print(len(list))
def bubble_sort_for(list):

    for i in range(1,len(list)):
        for j in range(0,len(list)-i):
            if list[j] > list[j+1]: #升序用>，降序用<
                list[j],list[j+1] = list[j+1],list[j]

    return list
if __name__ == '__main__':
    list1 = [6, 2, 3, 4, 5, 3, 9, 30, 133, 111]
    bubble_sort_for(list1)








