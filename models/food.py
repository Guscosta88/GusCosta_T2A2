from init import db
# This is one of the places where the init items are imported

# the class Food uses Sqlalchemy to create a table structure with column names and data types.
class Food(db.model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    type = db.Column(db.String)
    date = db.Column(db.Date)
    # wine_id
    # user_id
