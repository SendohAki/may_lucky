# -*- encoding=UTF-8 -*-

from nowstagram import db, login_manager
from datetime import datetime
import random

class Comment(db.Model):
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1024))
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer, default=0) # 0 正常 1 被删除
    user = db.relationship('User')

    def __init__(self, content, image_id, user_id):
        self.content = content
        self.image_id = image_id
        self.user_id = user_id

    def __repr__(self):
        return '<Comment %d %s>' % (self.id, self.content)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(512))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_date = db.Column(db.DateTime)
    comments = db.relationship('Comment')

    def __init__(self, url, user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime.now()

    def __repr__(self):
        return '<Image %d %s>' % (self.id, self.url)

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    salt = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    images = db.relationship('Image', backref='user', lazy='dynamic')

    def __init__(self, username, password, salt=''):
        self.username = username
        self.password = password
        self.salt = salt
        self.head_url = 'http://images.nowcoder.com/head/' + str(random.randint(0,1000)) +  'm.png'

    def __repr__(self):
        return '[User %d %s]' % (self.id, self.username)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
class User(db.Model):
    #__tablename__ = 'user'
    id = db.column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.column(db.String(20),unique=True)
    password = db.column(db.String(80))
    salt = db.column(db.String(50))
    head_url = db.column(db.String(250))
    images = db.relationship('Image',backref='user',lazy='dynamic')
    def __init__(self,user_name,password,salt=''):
        self.user_name = user_name
        self.password = password
        self.salt = salt
        self.head_url = 'http://images.nowcoder.com/head/' + str(random.randint(0,1000)) + '.png'

    def __repr__(self):
        return '[User %d %s]' %(self.id,self.user_name)


class Image(db.Model):
    __tablename__ = 'image'
    id  = db.column(db.Integer,primary_key=True,autoincrement=True)
    uesr_id = db.column(db.Integer,db.ForeignKey('user.id'))
    creaate_date = db.column(db.DateTime)
    url = db.column(db.String(250))
    comments = db.relationship('Comment',backref='image',lazy='dynamic')

    def __init__(self,user_id,create_time,url):
        self.user_id = user_id
        self.creaate_time = datetime.now()
        self.url = url
    def __repr__(self):
        return '[Image %d %s]' %(self.id,self.url)

class Comment(db.Model):
    id = db.column(db.Integer,primary_ket=True,autoincrement=True)
    image_id = db.column(db.Integer,db.ForeignKey('image.id'))
    user_id = db.column(db.Integer,db.ForeignKey('user.id'))
    content = db.column(db.String(512))
    status = db.column(db.Integer,default=0)
    user = db.relation('User')
    def __int__(self,image_id,user_id,content):
        self.image_id = image_id
        self.user_id = user_id
        self.content = content
    def __repr__(self):
        return '[Comment %d %s]' %(self.user_id,self.content)



print(User.query.all())
print(User.query.get(3))
print(User.query.filter_by(id=5).first())
print(User.query.order_by(User.id.desc()).offset(1).limit(2).all())
print(User.query.filter_by(id=50).update({'username':'sb'}))
db.session.commit()















