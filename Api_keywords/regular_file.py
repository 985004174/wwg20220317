# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/6/8 5:02 PM 
# ide： PyCharm
import re


def regular_file():
   str1='1,2,3,4,${token}'
   replace='asdf'
   new_str=re.sub('\$\{.*?\}',replace,str1)
   print(new_str)
if __name__ == '__main__':
    regular_file()