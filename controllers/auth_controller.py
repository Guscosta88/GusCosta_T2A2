from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from init import db, bcrypt
# This is one of the places where the init items are imported
from datetime import timedelta
from models.user import User, UserSchema
# The User class and UserSchema are imported here from models
from sqlalchemy.exc import IntegrityError
# this is a sqlalchemy error handler that handles the integrity of the data being send to the database.

# This is where the auth route url is defined in the blueprint to be registered in the main.
auth_db = Blueprint('auth',__name__,url_prefix='/auth')

# The Route bellow allows the user to access all users from the database.
@auth_db.route('/users/')
def get_users():
    # the function get_users retrieves all existing users using the select function to select the class User.
    stmt = db.select(User)
    # the session object handles the database and scalars (plural) filters the result into a rows.
    users = db.session.scalars(stmt)
    # the User schema and the dump converts the results into JSON that is displayed, excluding the password.
    return UserSchema(many=True, exclude=['password']).dump(users)


# The Route bellow allows the user to Register to the database.
@auth_db.route('/register/', methods=['POST'])
# The method POST Creates new items to be added to the database.
def auth_register():
    try:
        user = User(
            # Create a new User model instance from the user_info
            first_name=request.json.get('first_name'),
            last_name=request.json.get('last_name'),
            occupation=request.json.get('occupation'),
            email=request.json['email'],
            password=bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
            dob = request.json.get('dob')
        )
        # the session add, adds all of the above changes to the commit
        db.session.add(user)
        # the session commit pushes all of the above changes to the database
        db.session.commit()
        # the User schema and the dump converts the results into JSON that is displayed excluding the password.
        # the 201 status code is returned, which means that the request has been fulfilled and one or more new resources were created.
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'The email address entered already exists'}, 409
        # The integrity error handles the integrity of the data being send to the database, in this case an email that already exists.
        # The error 409 is a conflict error that happens due to data already in use.


# The Route bellow allows the user to Login.
@auth_db.route('/login/', methods=['POST'])
# The method POST Creates new items to be added to the database.
def auth_login():
    # the function auth_login finds an existing user in the database that matches the email address.
    stmt = db.select(User).filter_by(email=request.json['email'])
    # the session object handles the database and scalar (Singular) filters the result by email.
    user = db.session.scalar(stmt)
    # if the user email and password exists it creates a token and the user is logged in and allowed access.
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return {'email': user.email, 'token': token}
    else:
        return {'error': 'Invalid email or password provided'}, 401
        # if the user email and password does not exist a 401 of unauthorized access is returned





