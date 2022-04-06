# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/3/29 10:13 AM 
# ide： PyCharm
import json

import pytest

from config.url_config import URL_ADMIN


from Api_keywords.api_key import ApiKey


@pytest.fixture(scope='session')
def token_fix():
    "登录token"
    ak = ApiKey()
    token='1C1D9D030A3A4495BB95020206C62A5A'
    return ak, token
    # print(res.text)

@pytest.fixture(scope='session')
def token_admin():
    """
    后台token
    """
    ak = ApiKey()
    token='RbxM3O3RSvvTGzIohK/e/uw43Rtux8B79F3hRUAanTDCK8K45LBYBUmiCtyKEk2R38HMvA3icR0Y5VEnS/+kXL8q/G34j8DJf5MnZML70LOkvZl5m4h2UDmdOEhHLwaZlqyTqhJvHKqP0kOPTnZjlcUPfoMEPMWqwXeFdAalL8A='
    return ak,token


# if __name__ == '__main__':
#     token_fix()
