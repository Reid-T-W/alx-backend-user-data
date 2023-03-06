#!/usr/bin/env python3
""" Class to manage Authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Class to manage Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks of authuntication is required """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        # Making the method slash tolerent
        if path[-1] != '/':
            path = path + '/'

        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """ Handles the authorization header """
        if request is None:
            return None
        auth = request.headers.get("Authorization")
        if auth is None:
            return None
        return auth

    def current_user(self, request=None) -> TypeVar('User'):
        """ Handles current user """
        return None