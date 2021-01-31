from myblog import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:@127.0.0.1/myblog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import myblog.db.Blog
import myblog.db.User
import myblog.db.Tag
import myblog.db.Category
import myblog.db.Comment