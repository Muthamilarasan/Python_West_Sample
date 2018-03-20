from flask import Flask, request, jsonify
from spring_config_client import EnableAutoConfiguration
import os
import json

app = Flask(__name__)

port = int(os.getenv("PORT", 9099))
EnableAutoConfiguration(app, appname='pyconfig', profile='development', config_server=os.getenv('CONFIG_SERVER', None))


@app.route("/")
def welcome():
    return 'Welcome Config to Server!'

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
