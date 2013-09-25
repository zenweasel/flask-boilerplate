from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext.sqlalchemy import SQLAlchemy
from models import Post

app = Flask(__name__)
db = SQLAlchemy(app)

admin = Admin(app)
admin.add_view(ModelView(Post, db.session))