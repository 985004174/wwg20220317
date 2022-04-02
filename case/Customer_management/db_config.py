# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/3/30 4:45 PM 
# ide： PyCharm
import logging

import pymysql
import pytest
from pymysql.cursors import DictCursor


# @pytest.mark.parametrize('a,b',[(1,2),(3,4)])
# def test01(a,b):
#     print(a+b)

#
# if __name__ == '__main__':
#     pytest.main(['-s','db_config.py'])
#
#
#
# def demo(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# num_tuple = (1,2,3,4,5,6)
# # 元组
# student_info = {"name":"小明","age":12}
# # 字典
# print('---- 未拆包，即调用前不加星号，输出-----')
# demo(num_tuple,student_info)
#
#
# print('---- 拆包，即调用前加星号，输出：-----')
# demo(*num_tuple,**student_info)



# db_adress={host='',port=int(),name='',password=''}

db_adress={'host':'rm-wz9r8j008062a230r.mysql.rds.aliyuncs.com','database':'css_llp_one_stg','user':'hllcrm_dev','password':'sjnI6FCfHhF0YuJ8_IG3','port':3306}


# class db_action():
sql='select id,user_id,company_id,user_name from agent where user_id=398363'
class Db_Action():
    def __init__(self,db_adress):
        self.con=pymysql.connect(**db_adress)
    #   建立连接
        self.cursor=self.con.cursor(cursor=DictCursor)
    #   创建游标对象

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.con.close()

    def select(self,sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.con.ping(reconnect=True)
        # 执行sql
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # 查询所有结果
        print(result)
        #

    def excute(self,sql):
        """改/查/删"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.con.ping(reconnect=True)
            # 执行sql
            self.cursor.execute(sql)
            # 提交sql
            self.con.commit()
        except Exception as e:
            print("操作MySQL出现错误，错误原因：{}".format(e))
        # logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.con.rollback()

db=Db_Action(db_adress)









        # db_adress = {'host': 'rm-wz9r8j008062a230r.mysql.rds.aliyuncs.com', 'database': 'css_llp_one_stg',
        #              'user': 'hllcrm_dev', 'password': 'sjnI6FCfHhF0YuJ8_IG3', 'port': 3306}

def con_db(db_adress):
    # con = pymysql.connect(host='rm-wz9r8j008062a230r.mysql.rds.aliyuncs.com',database='css_llp_one_stg',user='hllcrm_dev',password='sjnI6FCfHhF0YuJ8_IG3',port=3306)
    con = pymysql.connect(**db_adress)
    # print(type(con))
    cursor=con.cursor(cursor=DictCursor)
    count=cursor.execute(sql)
    print(count)
    print(print("查询到%d条数据:" %count))
    result=cursor.fetchmany(3)
    print(result[0])
    print(result[0]['id'])
    cursor.close()
    con.close()
con_db(db_adress)
# for i in range(count):
#     result = cursor.fetchall()
#     print(result)
#
#     print(type(result))
# cursor.close()
# con.close()




# def db_execute(self,sql):
# #     pass
    # print(args)
    # print(kwargs)


