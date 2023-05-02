#!/usr/bin/python3
""" app_views blueprint for Flask API app """

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status/')
def status():
    """ Status JSON """
    return jsonify({"status": "OK"})


@app_views.route('/stats/')
def stats():
    """ Status JSON """
    return jsonify(storage.count())


@app_views.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Not found"}), 404
