from app import db, ma


class Restaurant(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    place = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    delivery = db.Column(db.Boolean)

    def __init__(self, name, category, place, address, phone, delivery, user_id):
        self.name = name
        self.category = category
        self.place = place
        self.address = address
        self.phone = phone
        # self.image_logo = image_logo
        # self.image_menu = image_menu
        self.delivery = delivery
        self.user_id = user_id

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "category": self.category,
            "place": self.place,
            "address": self.address,
            "phone": self.phone,
            "delivery": self.delivery,
        }

    @classmethod
    def get_restaurants_by_user(cls, user_id):
        query = cls.query.filter_by(user_id=user_id).all()
        return query


class Restaurant_Schema(ma.Schema):
    class Meta:
        fields = ("id", "name", "category", "place", "address", "phone", "delivery")


post_schema = Restaurant_Schema()
posts_schema = Restaurant_Schema(many=True)
