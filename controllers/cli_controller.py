from flask import Blueprint
from init import db, bcrypt
# This is one of the places where the init items are imported
# SQL Alchemy prevents from SQL injections, it sanitizes the queries on the background.

from datetime import date
from models.wine import Wine
from models.food import Food
from models.user import User
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
    users = [
        # Using the User class to add each row as a column to the table
        # the bcrypt module adds a layer of encryption enforced with the hash function and the decoder function
        User(
            first_name='Eddie',
            last_name='Osterland',
            occupation='Sommelier',
            email='eddieosterland@email.com',
            password=bcrypt.generate_password_hash('cabernet').decode('utf-8'),
            dob = '25/06/1954'
        ),
        User(
            first_name='Obi-Wan',
            last_name='Kenoby',
            occupation='Jedi',
            email='rebellion@email.com',
            password=bcrypt.generate_password_hash('shiraz').decode('utf-8'),
            dob = '57 BBY'
        ),
        User(
            first_name='Gordon',
            last_name='Ramsay',
            occupation='Chef',
            email='hellskitchen@email.com',
            password=bcrypt.generate_password_hash('merlot').decode('utf-8'),
            dob = '08/11/1966'
        )
    ]

    # the session add_all, adds all of the above changes to the commit
    db.session.add_all(users)
    # the session commit pushes all of the above changes to the database
    db.session.commit()

    wines = [
        # Using the Wine class to add each row as a column to the table
        Wine(
            name='Cabernet Sauvignon',
            description='Full-bodied wines with high tannins and noticeable acidity.',
            region='France, Bordeaux',
            type='Red Wine',
            date = date.today(),
            user = users[0]
        ),
        Wine(
            name='Shiraz',
            description='Spice, blue fruit, black fruit and pepper.',
            region='France, Rhone',
            type='Red Wine',
            date = date.today(),
            user = users[1]
        ),
        Wine(
            name='Merlot',
            description='blackberry, blueberry, plum, and/or raspberry.',
            region='France, Bordeaux',
            type='Red Wine',
            date = date.today(),
            user = users[2]
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
            date = date.today(),
            user = users[0],
            wine_id = 1
        ),
        Food(
            name='Barbeque',
            description='Sausages, kebabs and hearty vegetables that have a nice char from the grill.',
            type='Main',
            date = date.today(),
            user = users[1],
            wine_id = 2
        ),
        Food(
            name='Duck',
            description='Gordon\'s Roast Duck with pancakes and Dipping Sauce.',
            type='Main',
            date = date.today(),
            user = users[2],
            wine_id = 3
        )
    ]
    # the session add_all, adds all of the above changes to the commit
    db.session.add_all(foods)
    # the session commit pushes all of the above changes to the database
    db.session.commit()

    print('Tables Seeded')