from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.models import User
app = Flask(__name__)

db = SQLAlchemy()
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

pwd = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "You are mot authorised to access this page. Please login first."
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
from app import forms
from app import models
from app import views
from app import admin_views