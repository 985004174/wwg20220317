# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/13 11:08 AM 
# ide： PyCharm
import pytest
import yaml


def add(a, b):
    return a + b

def get_yaml():
    # 打开一个文件，生成文件流对象
    with open('../yaml_case/data01.yaml') as f:
        # 使用yaml解析文件流，生成一个Python可识别的数据类型
        data = yaml.load(f)
        print(data)
    return data

def test_get_yaml():
    get_yaml()

# 测试脚本
class TestAdd:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    # @pytest.mark.add
    @pytest.mark.parametrize("a, b,expect",get_yaml()["data"],ids=get_yaml()["ids"])
    def test_add(self, a, b, expect):
        assert expect == add(a, b)
