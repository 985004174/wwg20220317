# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/11 7:35 PM 
# ide： PyCharm
import pymysql
from pymysql.cursors import DictCursor

from log.logger_config import test_log

host=''

db_name=''
port=int(3306)
user=''
password=''

log=test_log()


# 创建一个数据库对象

class DB_action:


    def __init__(self):
        # 链接数据库
        self.con=pymysql.connect(host=host,database=db_name,port=port,user=user,password=password)
        # self.con
        # log.info('测试')
        # 创建一个字典游标
        self.cursor=self.con.cursor(pymysql.cursors.DictCursor)
        # log.info()

    def db_excute(self):
        # 执行操作
        self.cursor.execute(str(sql))

        # 查询出第一条结果
        result=self.cursor.fetchone()
        print(result)
        self.cursor.close()
        self.con.close()

    def select_record(self, query):
        """查询数据"""
        # 格式化字符串
        print("query:%s" % query)
        try:
            db_cursor = self.con.cursor()
            db_cursor.execute(query)
            result = db_cursor.fetchall()
            return result
        except Exception as e:
            print("执行数据库查询失败原因:%s" % e)
            self.cursor.close()
            exit()

    def execute_insert(self, query):
        """插入数据"""
        print("query:%s" % query)
        try:
            db_cursor = self.con.cursor()
            db_cursor.execute(query)

            db_cursor.excute("commit")
            return True
            # result=db_cursor.fetchall()
        # return result
        except Exception as e:
            print("执行数据库查询失败原因:%s" % e)
            self.cursor.execute("rollback")  # 回滚当前事务
            self.cursor.close()
            exit()

    def close(self):
        self.con.close()




if __name__ == '__main__':
    string = 123  # 类型为字符串
    print("string=%s" % string)  #

