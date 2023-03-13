#!/usr/bin/env python3
""" Authentication Module """
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound


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

    def register_user(self, email, password):
        """ Register a user """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pw = _hash_password(password)
            self._db.add_user(email, hashed_pw)
