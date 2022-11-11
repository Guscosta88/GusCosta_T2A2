from flask import Blueprint
from init import db

from flask_mail import Mail
# This is one of the places where the init items are imported
# SQL Alchemy prevents from SQL injections, it sanitizes the queries on the background.

from models.food import Food, FoodSchema


mail_db = Blueprint('send',__name__,url_prefix='/send')

mail = Mail(mail_db)

@mail_db.route("/")
def index():
    stmt = db.select(Food)
    foods = db.session.scalars(stmt)
    message_body = FoodSchema(many=True).dump(foods)
    msg = Message('Hello from the other side! find a suggestion of pairing', sender =   'guslfcosta@gmail.com', recipients = ['gustavo_leon88@hotmail.com'])
    msg.body = f"Hey, check my suggestion of pairing {message_body}"
    mail.send(msg)
    return "Message sent!"
