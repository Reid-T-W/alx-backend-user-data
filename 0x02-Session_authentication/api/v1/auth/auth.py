#!/usr/bin/env python3
""" Class to manage Authentication """
from flask import request
from typing import List, TypeVar
import re
import os


class Auth():
    """ Class to manage Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks of authuntication is required
            Returns:
                True if authentication is required
                    (path is not found in excluded_paths)
                False if authentication is not required
                    (path is found in excluded_paths)
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        # # Making the method slash tolerent
        if path[-1] != '/':
            path = path + '/'

        #  Allowing * at the end of excluded paths
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '*':
                excluded_path = excluded_path[:-1]
            match = re.match(excluded_path, path)
            # The case where a match is found.
            # The path has been found in the excluded list
            # Hence, authentication is not required
            if match is not None:
                return False
        return True

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

    def session_cookie(self, request=None) -> str:
        """ Returns a cookie value from a request """
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        cookie_value = request.cookies.get(cookie_name)
        return cookie_value
