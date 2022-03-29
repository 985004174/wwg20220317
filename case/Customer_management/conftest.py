# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/3/29 10:13 AM 
# ide： PyCharm
import json

import pytest

from config.url_config import URL


from Api_keywords.api_key import ApiKey


@pytest.fixture(scope='session')
def token_fix():
    ak = ApiKey()
    token='gEh3t9xmEafGujdcvXOm3JIpoLrs6Kf+ouWMu8Pwsr9FVPYu4gwgxm9UjixPGaUi+3mW8P5tQ2aW6G+1IuPBNQR3VcXWBnrxV2MY+fPmbnVi44kOJpPjvk6Ln+aFCZCirCXFDUWv31EjrP/ald7CwqXUYfmj9IEKoN582HlLQmw='
    # url = 'https://rbac-stg.huolala.cn/api/auth/login'
    # data = 'username=吴文光&password=19971024wwG&appid=hll-Fd8UszUhcwYL8Pr5'
    # # data1 = json.dumps(data)
    # hd = {'Content-Type':'application/x-www-form-urlencoded'}
    # res = ak.post(url, data=data,headers=hd )
    # res1 = ak.get(url1,)
    # print(res.text)
    # token = res.json()['token']
    # hd = {'token':token}
    # print(token1)
    # print(type(token1))
    # print(res.text)
    return ak,  token

# if __name__ == '__main__':
#     token_fix()
