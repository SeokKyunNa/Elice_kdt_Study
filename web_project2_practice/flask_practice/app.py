from db_connect import db
import config
import CrudTest
from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    api = Api(app)

    api.add_resource(CrudTest, '/', '<int:id>')


if __name__ == '__main__':
    create_app().run(debug=True, port=5000)

