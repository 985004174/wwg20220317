# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/5/31 5:25 PM 
# ide： PyCharm
import yaml
from yaml import FullLoader

# 封装yaml文件的常用操作行为
class Ymal_Control:
    # yaml文件读取
    def read_yaml(self,filepath):
        '''
        :param filepath: 文件路径
        :return: 返回读取到的数据
        '''
        # filepath=os.path.dirname(os.path.abspath(__file__))+'case.yaml'

        with open(file=filepath,mode='r') as f:
            data=yaml.load(stream=f,Loader = FullLoader)


            return data


if __name__ == '__main__':
    Ymal_Control().read_yaml('../case/yaml_Case/test1.yaml')



