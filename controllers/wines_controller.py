from flask import Blueprint
from init import db
from models.wine import Wine, WineSchema

wines_db = Blueprint('wines',__name__,url_prefix='/wines')

@wines_db.route('/')
def all_wines():
    stmt = db.select(Wine)
    wines = db.session.scalars(stmt)
    return WineSchema(many=True).dump(wines)
