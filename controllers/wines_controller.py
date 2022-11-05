from flask import Blueprint, request
from init import db
from datetime import date
# This is one of the places where the init items are imported
from models.wine import Wine, WineSchema
# The Wine class and WineSchema are imported here from models
from flask_jwt_extended import jwt_required, get_jwt_identity

# This is where the wines route url is defined in the blueprint to be registered in the main.
wines_db = Blueprint('wines',__name__,url_prefix='/wines')

# The Route bellow allows the user to access all wines from the database.
@wines_db.route('/')
def all_wines():
    # the function all_wines retrieves all existing wines using the select function to select the class Wine.
    stmt = db.select(Wine)
    # the session object handles the database and scalars (plural) filters the result into a rows.
    wines = db.session.scalars(stmt)
    # the Wine schema and the dump converts the results into JSON that is displayed.
    return WineSchema(many=True).dump(wines)


# The Route bellow allows the user to access one wine from the database.
@wines_db.route('/<int:id>/')
# The <int:id> specifies two things, a path converter (int) and a variable name to be captured (id).
def one_wine(id):
    # the function one_wine retrieve only one existing wine using the select function to select the class Wine and the filter_by to filter_by id.
    stmt = db.select(Wine).filter_by(id=id)
    # the session object handles the database and scalar (Singular) returns the matching result.
    wine = db.session.scalar(stmt)
    # the Wine schema and the dump converts the results into JSON that is displayed.
    return WineSchema().dump(wine)


# The Route bellow allows the user to access Delete one wine from the database.
@wines_db.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
# The <int:id> specifies two things, a path converter (int) and a variable name to be captured (id) and the http request method DELETE.
def delete_one_wine(id):
    # the function delete_one_wine retrieve only one wine using the select function to select the class Wine and the filter_by to filter_by id.
    stmt = db.select(Wine).filter_by(id=id)
    # the session object handles the database and scalar (Singular) returns the matching result.
    wine = db.session.scalar(stmt)
    # the Wine schema and the dump converts the results into JSON that is displayed.
    if wine:
        db.session.delete(wine)
        # the session commit pushes all of the above changes to the database, the delete, deletes the wine from the database.
        db.session.commit()
        return {'message': f'Wine "{wine.name}" deleted successfully'}
    else:
        # if the wine is not available a 404 not found error is returned
        return {'error': f'Could not delete, the wine with id {id} was not found'}, 404

# The Route bellow allows the user to Update one wine from the database.
@wines_db.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
# The <int:id> specifies two things, a path converter (int) and a variable name to be captured (id).
# The method PUT replaces the entire resource with given data, the PATCH only replaces specified fields.
def update_one_wine(id):
    # the function update_one_wine updates only one existing wine using the select function to select the class Wine and the filter_by to filter_by id.
    stmt = db.select(Wine).filter_by(id=id)
    # the session object handles the database and scalar (Singular) returns the matching result.
    wine = db.session.scalar(stmt)
    
    if wine:
        # The request json method get requests Json string from the server
        wine.name = request.json.get('name') or wine.name
        wine.description = request.json.get('description') or wine.description
        wine.region = request.json.get('region') or wine.region
        wine.type = request.json.get('type') or wine.type
        # the session commit pushes all of the above changes to the database
        db.session.commit()
        # the Wine schema and the dump converts the results into JSON that is displayed.
        return WineSchema().dump(wine)
    else:
        # if the wine is not available a 404 not found error is returned
        return {'error': f'Wine with id {id} was not found'}, 404


# The Route bellow allows the user to Create a new wine to the database.
@wines_db.route('/', methods=['POST'])
@jwt_required()
# The method POST Creates new items to be added to the database.
def create_wine():
    # the function create_wine creates one wine using the load function to load a POST method request json to the database.
        data = WineSchema().load(request.json)
    
        wine = Wine(
        # The request json method get requests Json string from the server
            name=data['name'],
            description=data['description'],
            region=data['region'],
            type=data['type'],
            date = date.today(),
            user_id = get_jwt_identity()
        )
        # the session add, adds all of the above changes to the commit
        db.session.add(wine)
        # the session commit pushes all of the above changes to the database
        db.session.commit()
        # the Wine schema and the dump converts the results into JSON that is displayed.
        # the 201 status code is returned, which means that the request has been fulfilled and one or more new resources were created.
        return WineSchema().dump(wine), 201







