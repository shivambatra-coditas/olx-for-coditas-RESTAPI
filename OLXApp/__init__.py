from flask import Flask
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt

# app object
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///olx.db"
app.config['SECRET_KEY'] = '085713473b8b19402dab5ffda6946710c81c1138'

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# bcrypt object
bcrypt = Bcrypt(app)

from OLXApp import apis

