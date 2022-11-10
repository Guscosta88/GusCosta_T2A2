from init import db, ma
# This is one of the places where the init items are imported

from marshmallow import fields


# the class User uses Sqlalchemy to create a table structure with column names and data types.
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    dob =db.Column(db.String, nullable=False)

    wines = db.relationship('Wine', back_populates='user', cascade='all, delete')
    foods = db.relationship('Food', back_populates='user', cascade='all, delete')

    # Marshmallow ma converts these data types into db readable format via the Schema and with the use of marshmallow fields each column item can be retrieved by the controller on a Model View Control (MVC) structure.
class UserSchema(ma.Schema):
    wines = fields.List(fields.Nested('WineSchema', only=['id','name']))
    foods = fields.List(fields.Nested('FoodSchema', only=['id','name']))
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'occupation', 'email', 'password', 'dob', 'wines', 'foods')
        ordered=True