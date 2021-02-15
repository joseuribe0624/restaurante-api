import os

from flask import Flask, jsonify, render_template, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
ma = Marshmallow(app)
api = Api(app)

from models.restaurant import Restaurant
from resources import restaurant, user

api.add_resource(user.Signup, "/signup")
api.add_resource(user.Login, "/login")

api.add_resource(restaurant.RestaurantsViews, "/restaurant")
api.add_resource(restaurant.RestaurantViews, "/restaurant/<int:restaurant_id>")
