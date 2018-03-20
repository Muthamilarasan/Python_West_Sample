import json
import requests
import os
from flask import make_response

if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
    access_token_uri = json.dumps(services['p-config-server'][0]['credentials']['access_token_uri']).strip('"')
    access_token_uri = access_token_uri+ '?grant_type=client_credentials'
    client_id = json.dumps(services['p-config-server'][0]['credentials']['client_id']).strip('"')
    client_secret = json.dumps(services['p-config-server'][0]['credentials']['client_secret']).strip('"')
    uri = json.dumps(services['p-config-server'][0]['credentials']['uri']).strip('"')
else:
    access_token_uri = dict(hostname='localhost', port=8888, password='')
    client_id = ""
    client_secret = ""
    uri = dict(hostname='localhost', port=8888, password='')

def EnableAutoConfiguration(app, appname, profile, config_server=None):

    print(access_token_uri)
    r = requests.post(access_token_uri, auth=(client_id, client_secret))
    json_res = json.loads(r.text)
    print(json_res)
    print(json_res['access_token'])
    accToken = 'bearer ' + json_res['access_token'];
    properties = requests.get('/'.join((uri, appname, profile)), headers={'Authorization': accToken}).json()
    app.config.update(properties)
    app.config['__spring_config_keys'] = properties.keys()

    @app.route('/env')
    def env():
        resp = make_response(json.dumps(dict([(k, app.config[k]) for k in app.config['__spring_config_keys']])))
        resp.headers['Content-Type'] = 'application/json'
        return resp
