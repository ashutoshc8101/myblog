from myblog.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(100))
    blogs = db.relationship('Blog', backref='created_by', lazy=True)
    comments = db.relationship('Comment', backref='created_by', lazy=True)

    def __repr__(self):
        return '<User id={} email={}'.format(self.id, self.email)
