#!/usr/bin/env python3
""" Module of session_auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:Dict representation of the user
    """
    # all_users = [user.to_json() for user in User.all()]
    # return jsonify(all_users)

    # Get email and password
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        return jsonify({"error": "email missing"}), 400

    if password is None:
        return jsonify({"error": "password missing"}), 400

    # Getting the user instance, search
    # returns a list, the first item is
    # the user instance
    user_list = User.search({"email": email})
    if len(user_list) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_list[0]
    if user.is_valid_password(password) is False:
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    resp = jsonify(user.to_json())
    resp.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return resp


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:empty dict if logout is successful
    """
    from api.v1.app import auth
    destroyed = auth.destroy_session(request)
    if destroyed is False:
        abort(404)
    return jsonify({}), 200
