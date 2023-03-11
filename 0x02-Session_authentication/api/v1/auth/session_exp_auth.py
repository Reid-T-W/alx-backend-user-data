#!/usr/bin/env python3
""" Session With expiary date """
from api.v1.auth.session_auth import SessionAuth
from api.v1.views.users import User
import uuid
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Session With expiary date """

    def __init__(self):
        """ Overiding init """
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Overloads the create_session method
        to support session expiration
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        created_at = datetime.now()
        self.user_id_by_session_id[session_id] = {'user_id': user_id,
                                                  'created_at': created_at}
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Overloading the user_id_for_session_id
        to support session expiration
        """
        if session_id is None:
            return None
        user = self.user_id_by_session_id.get(session_id)
        if user is None:
            return None
        if self.session_duration <= 0:
            # return list(user.keys())[0]
            user_id = user.get('user_id')
            return user_id

        created_at = user.get('created_at')
        if created_at is None:
            return None
        total_time = created_at + timedelta(seconds=self.session_duration)
        if total_time < datetime.now():
            return None
        return user.get('user_id')
