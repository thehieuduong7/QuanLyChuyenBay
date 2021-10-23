from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:tuan@1310@localhost/finalproj?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# Cần có key để thao tác với session
app.secret_key = "AG(ASDAGIA(*&!@"

#đặt tên j cx dc: PAGE_SIZE
#app.config["PAGE_SIZE"] = 3

db = SQLAlchemy(app=app)
admin = Admin(app=app, name = "MY SHOP", template_mode = 'bootstrap4')
my_login = LoginManager(app=app)
CART_KEY = "cart"