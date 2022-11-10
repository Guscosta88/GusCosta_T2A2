from flask import Flask
# Flask is used to create Python web applications

from init import db, ma, bcrypt, jwt
# This is one of the places where the init items are imported
# SQL Alchemy prevents from SQL injections, it sanitizes the queries on the background.

from controllers.wines_controller import wines_db
from controllers.foods_controller import foods_db
from controllers.auth_controller import auth_db
from controllers.cli_controller import db_commands
# the main controller commands are imported

from marshmallow.exceptions import ValidationError
# The ValidationError handler is responsible for handling an error when the user fails to respond to mandatory questions.
# it is an exception imported from Marshmallow
from sqlalchemy.exc import IntegrityError
# this is a sqlalchemy error handler that handles the integrity of the data being send to the database.

import os
# os is a module in python that fetches contents from underlying operating system.


def create_app():
    # This function is used so Flask knows where to look up for resources, templates, etc.
    # all of this app's functionality is centralized here.
    app = Flask(__name__)

    # The functions bellow handle the errors gracefully and return organized messages for better understanding and to facilitate troubleshooting.
    # The ValidationError handler is responsible for handling an error when the user fails to respond to mandatory questions.
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400

    # Handles errors caused by invalid http requests
    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400

    # Handles errors caused by not found http requests
    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404

    # It handles requests from unauthorized clients, due to lack of authentication information
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401

    # The IntegrityError handles errors when the id provided is not an existing foreign key from the requested table.
    @app.errorhandler(IntegrityError)
    def non_existing_id(err):
        return {'error': str(err)}, 500

    # The KeyError handles errors when the key necessary to access a dictionary is not found.
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The {err} needs to be provided'}, 400

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
    app.register_blueprint(foods_db)
    app.register_blueprint(auth_db)
    app.register_blueprint(db_commands)
    # this is where the controllers are resgistered to be able to run when the flask run command is called.

    return app