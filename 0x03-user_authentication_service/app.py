#!/usr/bin/env python3
""" Route module for app """
from flask import Flask, jsonify, request, abort, make_response, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_json() -> str:
    """ Gets a static json message """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """ Registers a user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """ Route for user login """
    email = request.form.get('email')
    password = request.form.get('password')

    # Checking if user is valid
    if not (AUTH.valid_login(email, password)):
        abort(401)
    # Creating session for a valid user
    session_id = AUTH.create_session(email)
    resp = make_response(jsonify({"email": f"{email}",
                                  "message": "logged in"}))
    resp.set_cookie('session_id', session_id)
    return resp


@app.route('/sessions', methods=['DELETE'])
def logout() -> None:
    """ Route for user logout """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    AUTH.destroy_session(user.id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
