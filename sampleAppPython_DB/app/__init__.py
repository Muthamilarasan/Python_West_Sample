# app/__init__.py

# third-party imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route("/create", methods=['POST'])
    def createContact():
        contact = repo.createContact(request.json)
        return contact, 200
        # if not request.json or not 'name' in request.json:
        #     abort(400)
        #
        # if len(contacts) <= 0:
        #     idValue = 0
        # else:
        #     idValue = contacts[-1]['id']+1
        #
        # contact = {
        # 'id':idValue,
        # 'name':request.json['name']
        # }
        # contacts.append(contact)
        # print (request.json['name'])
        # return jsonify(contacts), 200
    from app import models
    from app import repo
    return app
