from flask import Blueprint
from init import db
# This is one of the places where the init items are imported
from models.wine import Wine, WineSchema
# The Wine class and WineSchema are imported here from models

# This is where the wines route url is defined in the blueprint to be registered in the main.
wines_db = Blueprint('wines',__name__,url_prefix='/wines')

@wines_db.route('/')
def all_wines():
    # the function all_wines retrieves all existing wines using the select function to select the class Wine.
    stmt = db.select(Wine)
    # the session object handles the database and scalars (plural) filters the result into a rows.
    wines = db.session.scalars(stmt)
    # the Wine schema and the dump converts the results into JSON that is displayed.
    return WineSchema(many=True).dump(wines)



@wines_db.route('/<int:id>/')
# The <int:id> specifies two things, a path converter (int) and a variable name to be captured (id).
def one_wine(id):
    # the function one_wine retrieve only one existing wine using the select function to select the class Wine and the filter_by to filter_by id.
    stmt = db.select(Wine).filter_by(id=id)
    # the session object handles the database and scalar (Singular) returns the matching result.
    wine = db.session.scalar(stmt)
    # the Wine schema and the dump converts the results into JSON that is displayed.
    return WineSchema().dump(wine)



@wines_db.route('/<int:id>/', methods=['DELETE'])
# The <int:id> specifies two things, a path converter (int) and a variable name to be captured (id) and the http request method DELETE.
def delete_one_wine(id):
    # the function one_wine retrieve only one wine using the select function to select the class Wine and the filter_by to filter_by id.
    stmt = db.select(Wine).filter_by(id=id)
    # the session object handles the database and scalar (Singular) returns the matching result.
    wine = db.session.scalar(stmt)
    # the Wine schema and the dump converts the results into JSON that is displayed.
    if wine:
        db.session.delete(wine)
        db.session.commit()
        return {'message': f'Wine "{wine.name}" deleted successfully'}
    else:
        return {'error': f'Could not delete, the wine with id {id} was not found'}, 404



