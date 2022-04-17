# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/12 7:05 PM 
# ide： PyCharm
# data = '{"count": 2, "paytype": 1, "price": 100}'
# print(type(data))
# input_price = data[0]
# print(input_price)
import json

import pytest

# data = '{"count": 2, "paytype": 1, "price": 100}'
#
# str_list = data.split(sep=",", maxsplit=1)
# print(str_list)

# str1='{"count":1,"price"：100}'
# str2=json.loads(str1)
# print(str2)


# 同一个函数调用多次
from case_data.data_driver.yaml_driver import Read_Data

a=Read_Data()

# data=[(1,3),(2,4),(4,5)]
# ids=['case1','case2','case3']
#
# @pytest.mark.parametrize('a,b,c',a.get_yaml()['data'])
# def test_add(a,b,c):
#     print(a+b+c)

# @pytest.mark.parametrize("a, b,expect",get_yaml()["data"],ids=get_yaml()["ids"])
import pytest
# data = [('张三','男'),('李四','女'),('赵武','男')]

data1=[('张三','男','17'),('李四','女','20'),('赵武','男','24')]

data2=[[1, 2, 3], [0.5, 0.3, 0.8], [-0.1, 0.1, 0]]
case=['case1','case2','case3']
#需要按照某些条件或者数据进行入参时，可以按照这种方式
#'name,sex'表示入参的内容，data就是取值的列表，data1是值用例名称或标志
#data可以作为数据文件单独写一个文件
@pytest.mark.add
@pytest.mark.parametrize('name,sex,age',data2,ids=case)
def test_name(name,sex,age):
    print(name,sex,age)




#

