from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')  # 配置
db = SQLAlchemy(app)  # 初始化数据库
db.create_all()  # 创建表

from app import views
