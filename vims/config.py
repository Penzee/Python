# -*- coding: utf-8 -*-

import os

CSRF_ENABLED = True  # 激活跨站点请求伪造保护
SECRET_KEY = 'PrideZH'  # 密钥

# 数据库配置
basedir = os.path.abspath(os.path.dirname(__file__))  # 获得当前文件路径 
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mydb.db')  # 获得数据库路径
SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 每次请求结束都会自动提交事务
