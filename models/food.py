from init import db, ma
# This is one of the places where the init items are imported

from marshmallow import fields

# the class Food uses Sqlalchemy to create a table structure with column names and data types.
class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    wine_id = db.Column(db.Integer, db.ForeignKey('wines.id'))

    user = db.relationship("User", back_populates='foods')
    wine = db.relationship("Wine", back_populates='foods', cascade='all, delete')



# Marshmallow ma converts these data types into db readable format via the Schema and with the use of marshmallow fields each column item can be retrieved by the controller on a Model View Control (MVC) structure.
class FoodSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'first_name'])
    wine = fields.Nested('WineSchema', only=['id', 'name'])
    
    class Meta:
        fields = ('id', 'name', 'description', 'type', 'date', 'user', 'wine_id', 'wine')
        ordered=True