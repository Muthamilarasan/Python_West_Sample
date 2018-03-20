from flask import Flask, request
import os
from send import sendM
app = Flask(__name__)
port = int(os.getenv("PORT", 5000))

@app.route('/')
def sendMessage():
    return sendM();

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))
