# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/3/30 12:29 AM 
# ide： PyCharm
import os

import allure
import openpyxl


# def read():
import pytest

from Api_keywords.api_key import ApiKey

file = openpyxl.load_workbook('../data/data1.xlsx')

sheet = file['Sheet1']

print(sheet)
ak=ApiKey()

def read_excel():

    title_list=[]
    r_method_list=[]
    data_list=[]
    assert_list=[]
    except_value_list=[]

    for value in sheet.values:
        if type(value[0]) is int:

            # 用例标题
            title=value[10]
            # 请求参数
            data=value[5]
            # 校验字段
            assert_value=value[7]
            # 预期结果
            except_value=value[8]
            #
            r_method = [3]

            title_list.append(title)
            data_list.append(data)
            r_method_list.append(r_method)
            assert_list.append(assert_value)
            except_value_list.append(except_value)

            # print(title_list)
    return title_list,r_method_list,except_value_list,assert_list,data_list


# read_excel()

title_list, r_method_list, except_value_list, assert_list, data_list=read_excel()
list_tuple=list(zip(title_list,r_method_list))

@pytest.mark.parametrize('title_list,r_method_list',list_tuple)
def test01(title_list,r_method_list):
    # title_list,r_method_list = excel_data
    allure.dynamic.title(title_list)
    allure.dynamic.description(r_method_list)

    # return title,data,assert_value,except_value,dict_data


# def test_01():
#     res =getattr(ak,value[3])(**dict_data)
#
#     try:
#         result=ak.get_text(res.text,assert_value)
#         print('======实际结果=======')
#         print(result==except_value)
#
#     except:
#         print('======实际结果=======')
#         print('请求参数有误，请检查')

if __name__ == '__main__':
    # pytest.main(['-s','data_read.py'])
    pytest.main(['-s','data_read.py','--alluredir','./kevin','--clean-alluredir'])
    os.system('allure generate ./kevin -o ./report/ --clean')


