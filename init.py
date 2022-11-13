# Init file created to organize the main imports in a Dryer manner.

from flask_sqlalchemy import SQLAlchemy
# SQLAlchemy is an Object Relational Mapper (ORM) created to facilitate communication between
# Python and database, it also prevents from SQL injections, it sanitizes the queries on the background.

from flask_marshmallow import Marshmallow
# Marshmallow Is a library that converts to other data types to python data types

from flask_bcrypt import Bcrypt
# bcrypt is a password hashing function for encrypting.

from flask_jwt_extended import JWTManager
# Used to handle tokens


# stored in variables for easy access
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()







