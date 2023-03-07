#!/usr/bin/env python3
""" Class to manage Authentication """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class to manage Basic Authentication """
    