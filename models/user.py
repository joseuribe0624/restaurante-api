from app import bcrypt, db, ma


class User(db.Model):
    """
    #User Model Class
    """

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode()

    """
    #Save user details in Database
    """

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    """
    #Find user by username
    """

    @classmethod
    def exists_user(cls, username):
        return db.session.query(
            cls.query.filter_by(username=username).exists()
        ).scalar()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username")


post_schema = UserSchema()
posts_schema = UserSchema(many=True)
