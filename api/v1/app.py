#!/usr/bin/python3
""" Flask app for API package """

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def close_storge(error):
    # Close storage engine on exit
    storage.close()


if __name__ == "__main__":
    host, port = environ.get('HBNB_API_HOST'), environ.get('HBNB_API_PORT')
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = 5000
    app.run(debug=True, host=host, port=port, threaded=True)
