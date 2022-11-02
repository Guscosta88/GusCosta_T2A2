from flask import Blueprint
from init import db, bcrypt
# This is one of the places where the init items are imported
from datetime import date
from models.wine import Wine

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables Dropped")

@db_commands.cli.command('seed')
def seed_db():
    wines = [
        Wine(
            name='Cabernet Sauvignon',
            description='Full-bodied wines with high tannins and noticeable acidity.',
            region='France, Bordeaux',
            type='Red Wine',
            date = date.today()
        )
    ]

    db.session.add_all(wines)
    db.session.commit()

    print('Tables Seeded')