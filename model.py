from flask_sqlalchemy import SQLAlchemy                         #new: Flask-SQLAlchemy
from sqlalchemy import  Column, Integer, Text, TIMESTAMP
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    emails   = db.relationship('Email', backref='user', cascade="all, delete-orphan",lazy=True)
    
class Email(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    email   = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'),  nullable=False)
















# class User(db.Model):
#     id          = db.Column(db.Integer, primary_key=True)
#     username    = db.Column(db.Text, nullable=False)
#     email       = db.Column(db.Text, unique=True, nullable=False)
# 	##WARNING: SECURITY: Do NOT store a password like this: just for play here
#     password    = db.Column(db.Text, nullable=False)
#     created_at  = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)