from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from app import db
from models.restaurant import Restaurant, post_schema, posts_schema
from models.user import User


class RestaurantsViews(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        user = User.find_by_username(identity)
        restaurants = Restaurant.get_restaurants_by_user(user.id)
        return posts_schema.dump(restaurants)

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, type=str, location="json")
        parser.add_argument("category", required=True, type=str, location="json")
        parser.add_argument("place", required=True, type=str, location="json")
        parser.add_argument("address", required=True, type=str, location="json")
        parser.add_argument("phone", required=True, type=str, location="json")
        parser.add_argument("delivery", required=True, type=bool, location="json")
        data = parser.parse_args()

        categories = ["Gourmet", "Comida Rápida", "Comida Típica", "Autor"]
        if data["category"] not in categories:
            return {"message": "Invalid category"}, 400
        identity = get_jwt_identity()
        user = User.find_by_username(identity)
        try:
            new_restaurant = Restaurant(
                name=data["name"],
                category=data["category"],
                place=data["place"],
                address=data["address"],
                phone=data["phone"],
                delivery=data["delivery"],
                user_id=user.id,
            )
            db.session.add(new_restaurant)

            db.session.commit()

            return post_schema.dump(new_restaurant)
        except Exception as e:
            return str(e)


class RestaurantViews(Resource):
    @jwt_required()
    def get(self, restaurant_id):
        identity = get_jwt_identity()
        user = User.find_by_username(identity)
        restaurant = Restaurant.query.get_or_404(restaurant_id)
        if restaurant.user_id != user.id:
            return {"message": "Invalid restaurant"}, 403
        return post_schema.dump(restaurant)

    @jwt_required()
    def put(self, restaurant_id):
        identity = get_jwt_identity()
        user = User.find_by_username(identity)

        parser = reqparse.RequestParser()
        parser.add_argument("name", required=False, type=str, location="json")
        parser.add_argument("category", required=False, type=str, location="json")
        parser.add_argument("place", required=False, type=str, location="json")
        parser.add_argument("address", required=False, type=str, location="json")
        parser.add_argument("phone", required=False, type=str, location="json")
        parser.add_argument("delivery", required=False, type=bool, location="json")
        data = parser.parse_args()

        restaurant = Restaurant.query.get_or_404(restaurant_id)
        if restaurant.user_id != user.id:
            return {"message": "Invalid restaurant"}, 403

        categories = ["Gourmet", "Comida Rápida", "Comida Típica", "Autor"]
        if (
            "category" in data
            and data["category"]
            and data["category"] not in categories
        ):
            return {"message": "Invalid category"}, 400

        if "name" in data and data["name"]:
            restaurant.name = data["name"]
        if "category" in data and data["category"]:
            restaurant.category = data["category"]
        if "place" in data and data["place"]:
            restaurant.place = data["place"]
        if "address" in data and data["address"]:
            restaurant.address = data["address"]
        if "phone" in data and data["phone"]:
            restaurant.phone = data["phone"]
        if "delivery" in data and data["delivery"]:
            restaurant.delivery = data["delivery"]

        db.session.commit()
        return post_schema.dump(restaurant)

    @jwt_required()
    def delete(self, restaurant_id):
        identity = get_jwt_identity()
        user = User.find_by_username(identity)
        restaurant = Restaurant.query.get_or_404(restaurant_id)
        if restaurant.user_id != user.id:
            return {"message": "Invalid restaurant"}, 403
        db.session.delete(restaurant)
        db.session.commit()
        return "", 200


class ResourceRestaurantId(Resource):
    def get(self, id_):
        try:
            restaurant = Restaurant.query.get_or_404(id_)
            return posts_schema.dump(restaurant)
        except Exception as e:
            return str(e)
