#!/usr/bin/env python3
""" Authentication Module """
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union
from user import User


def _hash_password(password: str) -> bytes:
    """ Hash and return a password """
    binary_pw = password.encode('utf-8')
    hashed_pw = bcrypt.hashpw(binary_pw, bcrypt.gensalt())
    return hashed_pw


def _generate_uuid() -> str:
    """ Generates and returns a string representaiton of uuid """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initializer for Auth class """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a user """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pw = _hash_password(password)
            user = self._db.add_user(email, hashed_pw)
            return user

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

    def create_session(self, email: str) -> Union[str, None]:
        """ Creates a session for a user and returns the session id """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        # Generate a session id
        session_id = _generate_uuid()

        # Update the database with the users session id
        try:
            self._db.update_user(user.id, session_id=session_id)
        except ValueError:
            return None
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> Optional[str]:
        """ Gets a user given a session id """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """ Destorys a users session given a user_id """
        if user_id is None:
            return None
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            pass
        return None
