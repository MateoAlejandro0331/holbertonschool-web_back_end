#!/usr/bin/env python3
"""Flask app
"""
from flask import Flask, jsonify, abort, redirect, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome():
    """welcome route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Check if a user exists or creates a new one"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def sessions():
    """create a new session for the specified user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify(
                {"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
        abort(401)
    except BaseException:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout the user and destroy the session"""
    session_id = request.cookies.get('session_id')
    if session_id:
        user_id = AUTH.user_id_for_session_id(session_id)
        if user_id:
            AUTH.destroy_session(user_id)
            return redirect('/')
    return jsonify({'message': 'Forbidden'}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
