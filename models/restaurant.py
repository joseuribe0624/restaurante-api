from app import db
from app import ma


class Restaurant(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    #userId = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    name = db.Column(db.String(50)) 
    category = db.Column(db.String(50))
    place = db.Column(db.String(50)) 
    address = db.Column(db.String(50)) 
    phone = db.Column(db.String(50)) 
    delivery = db.Column(db.Boolean)

    def __init__(self, name, category, place, address, phone, delivery):
        self.name = name 
        self.category = category
        self.place = place
        self.address = address 
        self.phone = phone
        #self.image_logo = image_logo
        #self.image_menu = image_menu
        self.delivery = delivery

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name':self.name,
            'category':self.category, 
            'place':self.place,
            'address':self.address,
            'phone':self.phone,
            'delivery':self.delivery
        }

class Restaurant_Schema(ma.Schema):
    class Meta:
        fields = ("id", "name", "category", "place", "address", "phone", "delivery")

   

post_schema = Restaurant_Schema()

posts_schema = Restaurant_Schema(many = True)


# (las cuatro posibles categorías son: Gourmet,Comida Rápida, Comida Típica o de Autor)