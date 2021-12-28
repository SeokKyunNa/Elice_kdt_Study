from flask_restful import Resource, reqparse
from models import CrudTest
from db_connect import db

class CrudTest(Resource):
    def get(self):
        crud = CrudTest.query.filter(CrudTest.id == id).one()

        counter = crud.counter

        return counter
    
    def post(self):

        return 0

    
    def patch(self, id):

        return 0


    def delete(self, id):

        return 0