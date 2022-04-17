# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/11 5:27 PM 
# ide： PyCharm
import logging


def test2_log():
    logger=logging.getLogger()

    # 设定日志级别
    logger.setLevel(logging.DEBUG)

    # 日志处理器:1控制台处理器 2.文本处理器
    sh=logging.StreamHandler()
    logger.addHandler(sh)

    fh=logging.FileHandler('../webUI/web_log/log/ui_log.log',encoding='utf-8')
    logger.addHandler(fh)


    # 创建格式器
    fmt='%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s'
    fmt1='%(asctime)s %(filename)s %(levelname)s %(message)s'
    formatter=logging.Formatter(fmt)
    formatter1=logging.Formatter(fmt1)
    # 给相应的处理器设置格式
    sh.setFormatter(formatter)
    fh.setFormatter(formatter1)

    return logger
