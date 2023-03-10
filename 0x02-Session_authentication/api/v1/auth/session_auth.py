#!/usr/bin/env python3
""" Session Authenitcation Module """
from api.v1.auth.auth import Auth
from api.v1.views.users import User
import uuid
import os


class SessionAuth(Auth):
    """ Session Authenitcation Class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session_id given a user_id """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        # Generate session id
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a user_id given a session_id """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """ Get current user given request object """
        if request is None:
            return None
        auth_obj = Auth()
        cookie_value = auth_obj.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_value)
        user = User.get(user_id)
        return user
    
    def destroy_session(self, request=None):
        if request is None:
            return False
        cookie_value = self.session_cookie(request)
        if cookie_value is None:
            return False
        user_id = self.user_id_for_session_id(cookie_value)
        if user_id is None:
            return False
        del self.user_id_by_session_id[cookie_value]
        return True
