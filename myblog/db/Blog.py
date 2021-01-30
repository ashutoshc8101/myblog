from myblog.db import db

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    tags = db.Column(db.String(100))
    comments = db.Column(db.String(100))
    created_by = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime())

    def __repr__(self):
        return '<Blog %r>' % self.id


