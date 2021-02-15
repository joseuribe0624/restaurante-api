from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from app import bcrypt
from models.user import User

parser = reqparse.RequestParser()
parser.add_argument("username", required=True, type=str, location="json")
parser.add_argument("password", required=True, type=str, location="json")


class Signup(Resource):
    """
    User Registration Api
    """

    def post(self):
        data = parser.parse_args()
        username = data["username"]
        password = data["password"]
        if User.exists_user(username):
            return {"message": f"User {username} already exists"}

        new_user = User(username=username, password=password)
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=username)
            # refresh_token = create_refresh_token(identity=username)
            return {
                "message": f"User {username} was created",
                "access_token": access_token,
                # 'refresh_token': refresh_token
            }
        except:
            return {"message": "Something went wrong"}, 500


class Login(Resource):
    """
    User Login Api
    """

    def post(self):
        data = parser.parse_args()
        username = data["username"]
        current_user = User.find_by_username(username)
        if not current_user:
            return {"message": f"User {username} doesn't exist"}

        pw_hash = current_user.password
        candidate = data["password"]
        if bcrypt.check_password_hash(pw_hash, candidate):
            access_token = create_access_token(identity=username)
            return {
                "message": f"Logged in as {username}",
                "access_token": access_token,
            }
        else:
            return {"message": "Wrong credentials"}
