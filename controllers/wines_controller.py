from flask import Blueprint
from init import db


wines_db = Blueprint('wines',__name__,url_prefix='/wines')

@wines_db.route('/')
def all_wines():
    return 'wines test'
