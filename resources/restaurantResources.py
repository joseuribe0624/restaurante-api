from models.restaurant import Restaurant
from models.restaurant import post_schema
from models.restaurant import posts_schema


class ResourceRestaurant(Resource):
    def post(self):
        try:
            new_restaurant = Restaurant(
                name = request.json['name'],
                category = request.json['category'],
                place = request.json['place'],
                address = request.json['address'], 
                phone = request.json['phone'], 
               # image_logo = request.json['image_logo'],
               # image_menu = request.json['image_menu'],
                delivery = request.json['delivery']

            )
            db.session.add(new_restaurant)

            db.session.commit()

            return post_schema.dump(new_restaurant)
        except Exception as e:
            return(str(e))
    
    
    
class ResourceOneRestaurant(Resource):
    def get(self, id_):
        try:
            restaurant=Restaurant.query.get_or_404(id_)
            return post_schema.dump(restaurant)
        except Exception as e:
            return(str(e))

    def put(self, id_):
        try:
            restaurant = Restaurant.query.get_or_404(id_)
            if 'name' in request.json:
                restaurant.name = request.json['name']
            if 'category' in request.json:
                restaurant.category = request.json['category']
            if 'place' in request.json:
                restaurant.place = request.json['place']
            if 'address' in request.json:
                restaurant.address = request.json['address']
            if 'phone' in request.json:
                restaurant.phone = request.json['phone']
            if 'delivery' in request.json:
                restaurant.delivery = request.json['delivery']

            db.session.commit()
            return post_schema.dump(restaurant)
        except Exception as e:
            return(str(e))

    def delete(self, id_):
        try:
            restaurant = Restaurant.query.get_or_404(id_)
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        except Exception as e:
            return(str(e))

class ResourceRestaurantId(Resource):
    def get(self, id_):
        try:
            restaurant=Restaurant.query.get_or_404(id_)
            return posts_schema.dump(restaurant)
        except Exception as e:
            return(str(e))

api.add_resource(ResourceRestaurant, '/restaurant')      
api.add_resource(ResourceOneRestaurant, '/restaurant/<int:id_>')
api.add_resource(ResourceRestaurantId, '/get_all_restaurant/<int:id_>')