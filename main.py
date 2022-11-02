from flask import Flask
# Flask is used to create Python web applications

from init import db, ma, bcrypt, jwt
# This is one of the places where the init items are imported

from controllers.wines_controller import wines_db
from controllers.cli_controller import db_commands
# the main controller commands are imported

import os
# os is a module in python that fetches contents from underlying operating system.

def create_app():
    # This function is used so Flask knows where to look up for resources, templates, etc.
    # all of this app's functionality is centralized here.
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    # The configs are responsible for retrieving keys and paths from .env, .flaskenv files that are
    # safer if kept separated and not accessible, os helps retrieve these items.


    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    # This is where the imports from init are used to initialize the main application.

    app.register_blueprint(wines_db)
    app.register_blueprint(db_commands)
    # this is where the controllers are resgistered to be able to run when the flask run command is called.

    return app