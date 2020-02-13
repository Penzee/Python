# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField


class Car(FlaskForm):
    """添加车辆信息1"""
    type = StringField('型号')
    manufacturer = StringField('厂商')
    grade = StringField('等级')
    seat = IntegerField('座位数')
    displacement = FloatField('排量')
    gearbox = StringField('变速箱')
    colour = StringField('颜色')
    price = FloatField('价格')
    submit = SubmitField('确定')


class FindCar(FlaskForm):
    """查询车辆"""
    type = StringField('型号')
    manufacturer = StringField('厂商')
    grade = StringField('等级')
    seat = IntegerField('座位数')
    displacement = FloatField('排量')
    gearbox = StringField('变速箱')
    colour = StringField('颜色')
    price = FloatField('价格')
    submit = SubmitField('查询')
