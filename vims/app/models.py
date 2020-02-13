from app import db


class CarRole(db.Model):
    # 定义表名
    __tablename__ = 'cars'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True)  # 编号
    type = db.Column(db.String(16))  # 类型
    manufacturer = db.Column(db.String(16))  # 厂商
    grade = db.Column(db.String(16))  # 等级
    seat = db.Column(db.Integer)  # 座位数
    displacement = db.Column(db.Float)  # 排量
    gearbox = db.Column(db.String(16))  # 变速箱
    colour = db.Column(db.String(16))  # 颜色
    price = db.Column(db.Float)  # 价格

    def __repr__(self):
        return 'Car: %d %s' % (self.id, self.type)
