from typing import Counter
from db_connect import db

class CrudTest(db.Model):

    __tablename__ = 'crudtest'

    id      = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    counter = db.Column(db.String(20), nullable=False)

    def __init__(self, id, counter):
        self.id         = id
        self.counter    = counter
        