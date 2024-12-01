from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

routes = Blueprint('routes', __name__)

@routes.route('/articles', methods=['POST', 'DEL'])
@login_required
def articles():
    # Logic to update articles

    return jsonify({"message":"successfully updated article"})

@routes.route('/articles', methods=['GET'])
def get_articles():
    # Logic to get articles

    return jsonify({"message":"successfully retrieved articles"})

@routes.route('/projects', methods=['POST', 'DEL'])
@login_required
def projects():
    # Logic to update projects

    return jsonify({"message":"successfully updated projects"})

@routes.route('/projects', methods=['GET'])
def get_projects():
    # Logic to get projects

    return jsonify({"message":"successfully retrieved projects"})

@routes.route('/admin', methods=['GET'])
@login_required
def admin(): 

    return jsonify({"message":"successfully reached admin portal"})


@routes.route('/whoop', methods=['GET'])
@login_required
def whoop():  

    return jsonify({"message":"successfully reached whoop portal"})

@routes.route('/whoop/api', methods=['GET'])
@login_required
def whoop_api():  
    # Logic to generate and store api key for user

    return jsonify({"message":"successfully generated api key"})
