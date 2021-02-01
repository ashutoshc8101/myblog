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

@bp.route('/blogpost/<int:post_id>')
def blog_post(post_id):
    blog = Blog.query.filter_by(id=post_id).first()

    return render_template('blog_post.html', blog=blog)

@bp.route('/blog_entries', defaults={'page': 1})
@bp.route('/blog_entries/<int:page>')
def all_blogs(page):
    per_page = 8
    posts = Blog.query.order_by(Blog.created_at.desc()).paginate(page,per_page,error_out=False)
    return render_template('blog_entries.html', posts=posts.items)


@bp.route('/contact')
def contact():
    return render_template('contact.html')