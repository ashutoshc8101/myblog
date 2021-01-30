from myblog.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(100), )
