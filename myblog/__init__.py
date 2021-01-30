from flask import Flask
app = Flask(__name__)

from myblog.routes.home import bp as homebp
app.register_blueprint(homebp)