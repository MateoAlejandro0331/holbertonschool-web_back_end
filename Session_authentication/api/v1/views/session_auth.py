#!/usr/bin/env python3
""" Module of Session authentication views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email}) # search the user by email
    if user is False:
        return jsonify({"error": "no user found for this email"}), 404
    if user[0].is_valid_password(password) is False:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    auth.create_session(user[0].id)
    user_json = jsonify(user[0].to_json())
    cookie_value = auth.session_cookie(request)
    cookie_name = str(getenv('SESSION_NAME'))
    user_json.set_cookie(cookie_name, cookie_value)
    return  user_json


