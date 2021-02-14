from app import db

class Restaurant(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    #userId = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    name = db.Column(db.String(50)) 
    category = db.Column(db.String(50))
    place = db.Column(db.String(50)) 
    address = db.Column(db.String(50)) 
    phone = db.Column(db.String(50)) 
    image_logo = db.Column(db.String(200))
    image_menu = db.Column(db.String(200))
    delivery = db.Column(db.Boolean)

    def __init__(self, name, category, place, address, phone, image_logo, image_menu, delivery):
        self.name = name 
        self.category = category
        self.place = place
        self.address = address 
        self.phone = phone
        self.image_logo = image_logo
        self.image_menu = image_menu
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
            'image_logo':self.image_logo,
            'image_menu':self.image_menu,
            'delivery':self.delivery
        }


# (las cuatro posibles categorías son: Gourmet,Comida Rápida, Comida Típica o de Autor)