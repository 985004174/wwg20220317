# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/12 12:42 PM 
# ide： PyCharm
import json

import pytest
import yaml

from log.logger_config import test2_log

"""
打开yaml文件，解析为list
"""

class Read_Data():


        # self.file = open('../yaml_case/data01.yaml', 'r', encoding='utf8')


    def read_yaml(self):
        # log = test2_log()
        """
        :param filepath: 文件路径（相对路径）
        :return: list
        """
        try:
            # log=test2_log()
            # 指定文件
            # filepath = '../yaml_case/data01.yaml'
            file = open('../yaml_case/data01.yaml','r',encoding='utf8')

            # 读取文件中的内容
            data = yaml.load(stream=file,Loader=yaml.FullLoader)
            log = test2_log()
            log.info('data:{}'.format(data))
            # print(data)
            # print(data['ids'])
            # print(data)
            return data

        except Exception as e:
            print('当前路径下没有文件{}，请确认文件是否存在'.format(e))





if __name__ == '__main__':
    A=Read_Data()


