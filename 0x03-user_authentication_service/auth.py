#!/usr/bin/env python3
""" Authentication Module """
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Hash and return a password """
    binary_pw = password.encode('utf-8')
    hashed_pw = bcrypt.hashpw(binary_pw, bcrypt.gensalt())
    return hashed_pw


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initializer for Auth class """
        self._db = DB()

    def register_user(self, email: str, password: str):
        """ Register a user """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pw = _hash_password(password)
            self._db.add_user(email, hashed_pw)

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates the user trying to login """
        # Check if the user exists and retrieve the password
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        # Check if the password is correct
        encoded_pw = password.encode('utf-8')
        if bcrypt.checkpw(encoded_pw, user.hashed_password):
            return True
        return False

    def _generate_uuid(self) -> str:
        """ Generates and returns a string representaiton of uuid """
        return str(uuid.uuid4())
