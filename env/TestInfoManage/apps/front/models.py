from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import config
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DB_URI=config.DB_URI
engine=create_engine(DB_URI)
Base=declarative_base(engine)
session=sessionmaker(engine)()

#用户model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    _password = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password,email):
        self.username = username
        self.password = password
        self.email=email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self._password, raw_password)
        return result

#部门model
class ProjectModel(db.Model):
    __tablename__='project'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    project=db.Column(db.String(20),nullable=False,unique=True,comment='项目名')
    projectdescription=db.Column(db.String(100),nullable=True,comment='项目描述')
    creator=db.Column(db.String(20),nullable=False,comment='创建者')
    join_time=db.Column(db.DateTime,default=datetime.now,comment='更新时间')

    def