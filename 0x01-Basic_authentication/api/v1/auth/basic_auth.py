#!/usr/bin/env python3
""" Class to manage Authentication """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """ Class to manage Basic Authentication """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract base64 authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        # Checking if the authorization_header starts with the word basic
        if re.match(r'Basic .*', authorization_header) is None:
            return None
        # Returning the value after basic
        return (re.search(r'(?<=Basic ).*', authorization_header).group(0))
