from flask import Blueprint
from init import db, bcrypt
# This is one of the places where the init items are imported
from datetime import date
from models.wine import Wine
from models.food import Food
# The classes and Schemas are imported here from models

# This is where the commands route url is defined in the blueprint to be registered in the main.
db_commands = Blueprint('db', __name__)

# the function create_db creates Tables using the create_all function that uses a CLI command to send json to the database and prints a message to the terminal that the tables were created.
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables Created")

# the function drop_db drops Tables using the drop_all function that uses a CLI command to remove json from the database and prints a message to the terminal that the tables were dropped.
@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables Dropped")

# the function seed_db Adds data to the table columns using the add_all function that uses a CLI command to send json to the database and prints a message to the terminal that the tables were seeded.
@db_commands.cli.command('seed')
def seed_db():
    wines = [
        # Using the Wine class to add each row as a column to the table
        Wine(
            name='Cabernet Sauvignon',
            description='Full-bodied wines with high tannins and noticeable acidity.',
            region='France, Bordeaux',
            type='Red Wine',
            date = date.today()
        )
    ]

    # the session add_all, adds all of the above changes to the commit
    db.session.add_all(wines)
    # the session commit pushes all of the above changes to the database
    db.session.commit()

    foods = [
        # Using the Wine class to add each row as a column to the table
        Food(
            name='Steak',
            description='T-Bone Steak with mash potatoes and mushroom sauce',
            type='Main',
            date = date.today()
        )
    ]
    # the session add_all, adds all of the above changes to the commit
    db.session.add_all(foods)
    # the session commit pushes all of the above changes to the database
    db.session.commit()

    print('Tables Seeded')