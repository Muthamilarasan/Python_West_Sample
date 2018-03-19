from flask import Flask, request, jsonify
from db import db_session, initial_db
from models import Contact
import os
import json
app = Flask(__name__)
port = int(os.getenv("PORT", 5000))
@app.route('/')
def hello_world():
    return "Hello World"
    # if 'VCAP_SERVICES' in os.environ:
        # return os.getenv('VCAP_SERVICES');
        # services = os.getenv('VCAP_SERVICES')
        # services = json.loads(os.getenv('VCAP_SERVICES'))
        # return jsonify(services['p-mysql'][0]['credentials']['uri'])
        # mysql_env = services['p-mysql'][0]['credentials']
        # return mysql_env;


@app.route("/create", methods=['POST'])
def createContact():
    initial_db()
    c = Contact(request.json['name'])
    db_session.add(c)
    db_session.commit()
    print(db_session.query(Contact).all())
    return jsonify(json_list=[i.serialize for i in db_session.query(Contact).all()]),200

@app.route("/getAll", methods=['GET'])
def getAllContacts():
    initial_db()
    return jsonify(json_list=[i.serialize for i in db_session.query(Contact).all()]),200

@app.route("/updateContact", methods=['PUT'])
def updateContact():
    initial_db()

    print(db_session.query(Contact).filter(Contact.name == request.json['name']).filter(Contact.id == request.json['id']).all())
    db_session.query(Contact).filter(Contact.id == request.json['id']).update({Contact.name: request.json['name']}, synchronize_session=False)
    return jsonify(json_list=[i.serialize for i in db_session.query(Contact).all()]),200

@app.route("/deleteContact/<contactID>", methods=['DELETE'])
def deleteContact(contactID):
    initial_db()

    db_session.query(Contact).filter(Contact.id == int(contactID)).delete(synchronize_session=False)
    return jsonify(json_list=[i.serialize for i in db_session.query(Contact).filter(Contact.id == int(contactID)).all()]),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))
