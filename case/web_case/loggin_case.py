# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/12 9:57 AM 
# ide： PyCharm
import pytest

from api_keyword.base_word import KeyWord
from config.enviroment import URL

# http://39.98.138.157:5000/api/login
class Test_Logging():
    # def __init__(self):
    #     self.ak=KeyWord()
    def test_get_userinfo(self,get_token):
        token, res = get_token
        ak=KeyWord()
        url='http://39.98.138.157:5000/api/getuserinfo'
        hd={'token':token, 'content-type': 'application/json' }
        res2 = ak.get(url,headers=hd)
        print(res2.text)




        # except Exception as e:
        #     print('登录失败:{}'.format(e))




if __name__ == '__main__':
    pytest.main(['-s','logging_case.py'])

