from flask import Flask, request, jsonify
import os

app = Flask(__name__)

port = int(os.getenv("PORT", 9099))

contacts = [];

@app.route("/")
def welcome():
    return 'Welcome Msg!'

@app.route("/create", methods=['POST'])
def createContact():
    if not request.json or not 'name' in request.json:
        abort(400)

    if len(contacts) <= 0:
        idValue = 0
    else:
        idValue = contacts[-1]['id']+1

    contact = {
    'id':idValue,
    'name':request.json['name']
    }
    contacts.append(contact)
    print (request.json['name'])
    return jsonify(contacts), 200

@app.route("/getAllContacts", methods=['GET'])
def getAllContacts():
    return jsonify(contacts),200

@app.route("/contacts/<contactID>", methods=['GET'])
def getContact(contactID):
    con = [contact for contact in contacts if contact['id'] == int(contactID)]
    return jsonify(con),200;

@app.route("/updateContact/<contactID>", methods=['PUT'])
def updateContact(contactID):
    if not request.json or not 'name' in request.json:
        abort(400)
    contact = [contact for contact in contacts if contact['id'] == int(contactID)]
    if len(contacts) <= 0:
        abort(400)
    if 'name' in request.json :
        contact[0]['name'] = request.json['name']
    return jsonify(contact),200

@app.route("/deleteContact/<contactID>", methods=['DELETE'])
def deleteContact(contactID):
    contact = [contact for contact in contacts if contact['id'] == int(contactID)]
    if len(contacts) <= 0:
        abort(404)

    contacts.remove(contact[0])
    return 'Deleted',200


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
