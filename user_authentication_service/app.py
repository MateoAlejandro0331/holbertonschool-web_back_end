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
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect('/')
    return jsonify({'message': 'Forbidden'}), 403


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """Get the profile of the user"""
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({'email': user.email}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """Route to reset token password"""
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
        if token:
            return jsonify({"email": email, "reset_token": token})
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """Update user password endpoint"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, email, new_password)
        return jsonify({'email': email, 'message': 'Password updated'}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
