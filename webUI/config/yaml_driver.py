# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/15 4:25 PM 
# ide： PyCharm
import yaml

file='../data/data1.yaml'


def read_yaml():
    try:
        file1=open('../data/data1.yaml','r',encoding='utf-8')

        data=yaml.load(stream=file1,Loader=yaml.FullLoader)
        return data
    except Exception as e:
        print(e)

if __name__ == '__main__':
    read_yaml()