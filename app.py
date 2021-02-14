import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import restaurant


"""class ResourceRestaurant(Resource):

    def create_restaurant(self):
        name = request.args.get('name')
        category = request.args.get('category')
        place = request.args.get('place') 
        address = request.args.get('address') 
        phone = request.args.get('phone') 
        image_logo = request.args.get('image_logo')
        image_menu = request.args.get('image_menu')
        delivery = request.args.get('delivery')
        try:
            restaurant=restaurant(
                name = name,
                category = category,
                place = place,
                address = address,
                phone = phone,
                image_logo = image_logo,
                image_menu = image_menu,
                delivery = delivery
            )
            db.session.add(restaurant)
            db.session.commit()
            return "restaurant added. restaurant id={}".format(restaurant.id)
        except Exception as e:
            return(str(e))

  
    def get_all(self, userId_):
        try:
            restaurant=Restaurant.query.filter_by(userId=userId_).all()
            #restaurants=Restaurant.query.all()
            return  jsonify([e.serialize() for e in restaurants])
        except Exception as e:
            return(str(e))

   
    def get_by_id(self,id_):
        try:
            restaurant=Restaurant.query.filter_by(id=id_).first()
            return jsonify(book.serialize())
        except Exception as e:
            return(str(e))



api.add_resource(ResourceRestaurant, '/create_restaurant')      
api.add_resource(ResourceRestaurant, '/getall_restaurant/<int:userId_>')
api.add_resource(ResourceRestaurant, '/get_by_user_id/<int:id_>')"""



if __name__ == '__main__':
    app.run()