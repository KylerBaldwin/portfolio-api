import json
from os import getenv
import requests as r

from flask import Blueprint, request, jsonify, redirect
from flask_login import login_required, current_user

from . import db

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

@routes.route('/whoop/auth', methods=['GET'])
@login_required
def whoop_auth():
# Get the Whoop app URL from the environment variable
    whoop_app = getenv('WHOOP_APP_URL')

    # Prepare login credentials (you may need to get these from your session or database)
    login_data = {
        'username': current_user.username,
        'password': current_user.password
    }

    login_url = f'https://{whoop_app}/login'
    auth_url = f'https://{whoop_app}/whoop/auth?user_id={current_user.id}'
    
    try:
        # Send the POST request to Whoop to login
        res = r.post(login_url, data=login_data)

        # Check if the login was successful
        if res.status_code == 200:
            return redirect(auth_url)
        else:
            return jsonify({"message": "Login failed", "error": res.text}), 400
    except Exception as e:
        return jsonify({"message": "Error during authentication", "error": str(e)}), 500

@routes.route('/whoop/api', methods=['GET'])
@login_required
def whoop_api():  
    # Logic to generate and store api key for user

    return jsonify({"message":"successfully generated api key"})
