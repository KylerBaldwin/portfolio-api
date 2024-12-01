from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import json


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = json.loads(request.data) 
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                #Redirect to admin portal
                return jsonify({"message":"Successfully logged in"})
            else:
                return jsonify({"message":"incorrect password, please try again"})
        else:
            return jsonify({"message":"User does not exist"})
    # Redirect to home
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    # Redirect to home
    return jsonify({"message":"Successfully logged out"})


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        data = json.loads(request.data) 
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            login_user(user, remember=True)
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            #Redirect to admin portal
            return redirect(url_for('routes.admin'))
    # Send to sign up page
    return render_template("sign_up.html", user=current_user)
