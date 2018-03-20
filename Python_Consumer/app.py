from flask import Flask, request
import os
from receive import *
app = Flask(__name__)
port = int(os.getenv("PORT", 5000))

@app.route('/')
def Hello():
    return "Hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))
