from init import db, ma
# This is one of the places where the init items are imported

from marshmallow import fields

# the class Wine uses Sqlalchemy to create a table structure with column names and data types.
class Wine(db.Model):
    __tablename__ = 'wines'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    region = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    # user_id

# Marshmallow ma converts these data types into db readable format via the Schema and with the use of marshmallow fields each column item can be retrieved by the controller on a Model View Control (MVC) structure.
class WineSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'region', 'type', 'date')