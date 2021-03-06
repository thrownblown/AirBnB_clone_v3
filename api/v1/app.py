#!/usr/bin/python3
""" flask app web server listening on 0.0.0.0 on port 5000 """
import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_app(resp):
    """ closes db connection """
    storage.close()


@app.errorhandler(404)
def _handle_api_error(ex):
    """ returns json 404 """
    return (jsonify({'error': 'Not found'}), 404)


HOST = os.getenv('HBNB_API_HOST', '0.0.0.0')
PORT = os.getenv('HBNB_API_PORT', '5000')

if __name__ == "__main__":
    app.run(host=HOST, port=int(PORT), threaded=True)
