from flask import Blueprint, request
from init import db
from datetime import date
# This is one of the places where the init items are imported
from models.food import Food, FoodSchema
# The Food class and FoodSchema are imported here from models
from flask_jwt_extended import jwt_required, get_jwt_identity

# This is where the foods route url is defined in the blueprint to be registered in the main.
foods_db = Blueprint('foods',__name__,url_prefix='/foods')

# The Route bellow allows the user to access all foods from the database.
@foods_db.route('/')
def all_foods():
    # the function all_foods retrieves all existing foods using the select function to select the class Food.
    stmt = db.select(Food)
    # the session object handles the database and scalars (plural) filters the result into a rows.
    foods = db.session.scalars(stmt)
    # the Food schema and the dump converts the results into JSON that is displayed.
    return FoodSchema(many=True).dump(foods)


# The Route bellow allows the user to access one food from the database.
@foods_db.route('/<int:id>/')
# The <int:id> specifies two things, a path converter (int) and a variable name to be captured (id).
def one_food(id):
    # the function one_food retrieve only one existing food using the select function to select the class Food and the filter_by to filter_by id.
    stmt = db.select(Food).filter_by(id=id)
    # the session object handles the database and scalar (Singular) returns the matching result.
    food = db.session.scalar(stmt)
    # the Food schema and the dump converts the results into JSON that is displayed.
    return FoodSchema().dump(food)


# The Route bellow allows the user to access Delete one food from the database.
@foods_db.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
# The <int:id> specifies two things, a path converter (int) and a variable name to be captured (id) and the http request method DELETE.
def delete_one_food(id):
    # the function delete one_food retrieve only one food using the select function to select the class Food and the filter_by to filter_by id.
    stmt = db.select(Food).filter_by(id=id)
    # the session object handles the database and scalar (Singular) returns the matching result.
    food = db.session.scalar(stmt)
    # the Food schema and the dump converts the results into JSON that is displayed.
    if food:
        db.session.delete(food)
        # the session commit pushes all of the above changes to the database, the delete, deletes the food from the database.
        db.session.commit()
        return {'message': f'Food "{food.name}" deleted successfully'}
    else:
        # if the food is not available a 404 not found error is returned
        return {'error': f'Could not delete, the food with id {id} was not found'}, 404

# The Route bellow allows the user to Update one food from the database.
@foods_db.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
# The <int:id> specifies two things, a path converter (int) and a variable name to be captured (id).
# The method PUT replaces the entire resource with given data, the PATCH only replaces specified fields.
def update_one_food(id):
    # the function update_one_food updates only one existing food using the select function to select the class Food and the filter_by to filter_by id.
    stmt = db.select(Food).filter_by(id=id)
    # the session object handles the database and scalar (Singular) returns the matching result.
    food = db.session.scalar(stmt)
    
    if food:
        # The request json method get requests Json string from the server
        food.name = request.json.get('name') or food.name
        food.description = request.json.get('description') or food.description
        food.type = request.json.get('type') or food.type
        food.wine_id = request.json.get('wine_id') or food.wine_id
        # the session commit pushes all of the above changes to the database
        db.session.commit()
        # the Food schema and the dump converts the results into JSON that is displayed.
        return FoodSchema().dump(food)
    else:
        # if the food is not available a 404 not found error is returned
        return {'error': f'Food with id {id} was not found'}, 404


# The Route bellow allows the user to Create a new food to the database.
@foods_db.route('/', methods=['POST'])
@jwt_required()
# The method POST Creates new items to be added to the database.
def create_food():
    # the function create_food creates one food using the load function to load a POST method request json to the database.
        data = FoodSchema().load(request.json)
    
        food = Food(
        # The request json method get requests Json string from the server
            name=data['name'],
            description=data['description'],
            type=data['type'],
            date = date.today(),
            user_id = get_jwt_identity(),
            wine_id = data['wine_id']
        )
        # the session add, adds all of the above changes to the commit
        db.session.add(food)
        # the session commit pushes all of the above changes to the database
        db.session.commit()
        # the Food schema and the dump converts the results into JSON that is displayed.
        # the 201 status code is returned, which means that the request has been fulfilled and one or more new resources were created.
        return FoodSchema().dump(food), 201







