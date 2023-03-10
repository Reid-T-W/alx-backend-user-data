#!/usr/bin/env python3
""" Session saved to db """
from api.v1.auth.session_auth import SessionExpAuth
from api.v1.views.users import User
import uuid
import os
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ Session With expiary date """

    def create_session(self, user_id=None):
        """ Overiding init """
        session_id = super(user_id)

    def user_id_for_session_id(self, session_id=None):
        """ Overriding user_id_for_session_id"""
        ...
        user_id = super(session_id)

    def destroy_session(self, request=None):
        """ Overridingdestroy_session """
        ...
        destroyed_session = super(request)
