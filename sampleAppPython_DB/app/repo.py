from app import db

def createContact(json):
    if not json or not 'name' in json:
        abort(400)

    db.session.add(json)
    db.session.commit()
    return json, 200
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
    # print("dddddtesttt")
    # return "Hello"
