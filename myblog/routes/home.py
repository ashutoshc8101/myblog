from flask import Blueprint, render_template
from myblog.db.Blog import Blog
bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    blogs = Blog.query.order_by(Blog.created_at.desc()).limit(6).all()
    return render_template('index.html', blogs=blogs)

@bp.route('/about')
def about():
    return render_template('about.html')