from myblog.db import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(400), nullable=True)
    blogs = db.relationship('Blog', backref='category', lazy=True)

    def __repr__(self):
        return '<Category id={} title={} >'.format(self.id, self.title)