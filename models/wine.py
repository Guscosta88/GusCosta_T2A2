from init import db

class Wine(db.model):
    __tablename__ = 'wines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    region = db.Column(db.String)
    type = db.Column(db.String)
    date = db.Column(db.Date)
    # user_id