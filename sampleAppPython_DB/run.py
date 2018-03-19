# run.py

import os


from app import create_app

config_name = os.getenv('FLASK_CONFIG')
# app = create_app(config_name)
port = int(os.getenv("PORT", 9099))
app = create_app('production')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))
