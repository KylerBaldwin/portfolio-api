from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class WhoopAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    refresh_token = db.Column(db.String(250), nullable=True)
    api_key = db.Column(db.String(250), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250))
    username = db.Column(db.String(150))
    WhoopAuth = db.relationship('WhoopAuth')
