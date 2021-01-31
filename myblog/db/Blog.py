from myblog.db import db
from myblog.db.Tag import tags

class Blog(db.Model):

    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('blogs', lazy=True))
    comments = db.relationship('Comment', backref='blog', lazy=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return '<Blog %r>' % self.id


