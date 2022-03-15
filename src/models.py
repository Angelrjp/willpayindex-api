from sqlalchemy.orm import backref
from extensions import db

# Models
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html
class UserInfo(db.Model):
    __tablename__ = "T_USER_INFO"   
    
    user_id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(6))
    phone = db.Column(db.String(50))
    city = db.Column(db.String(128))

class UserIncome(db.Model):
    __tablename__ = "T_USER_INCOME"
    
    id = db.Column(db.Integer, primary_key=True)
    monthly_income = db.Column(db.Float)
    monthly_expenses = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('T_USER_INFO.user_id'))
    user = db.relationship("UserInfo", backref=backref("income", uselist=False)) # https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-one
