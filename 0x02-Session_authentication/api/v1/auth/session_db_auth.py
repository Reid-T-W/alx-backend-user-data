#!/usr/bin/env python3
""" Session saved to db """
from api.v1.auth.session_exp_auth import SessionExpAuth
from api.v1.views.users import User
from models.user_session import UserSession
import uuid
import os
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ Session With expiary date """

    def create_session(self, user_id=None):
        """ Overiding init """
        session_id = super().create_session(user_id)
        self.user_session = UserSession(user_id=user_id,
                                        session_id=session_id)
        self.user_session.save()
        return (session_id)

    def user_id_for_session_id(self, session_id=None):
        """ Overriding user_id_for_session_id"""
        if session_id is None:
            return None
        UserSession.load_from_file()
        dicts = UserSession.all()
        user_id = None
        for dict in dicts:
            if dict.session_id == session_id:
                correct_dict = dict
                user_id = dict.user_id
                break
        if user_id is None:
            return None
        if self.session_duration <= 0:
            return user_id
        created_at = correct_dict.created_at
        if created_at is None:
            return None
        total_time = created_at + timedelta(seconds=self.session_duration)
        if total_time < datetime.utcnow():
            return None
        return user_id

    def destroy_session(self, request=None):
        """ Overridingdestroy_session """
        if request is None:
            return False

        # cookie_value is the session_id
        cookie_value = self.session_cookie(request)
        if cookie_value is None:
            return False
        # user_id = self.user_id_for_session_id(cookie_value)
        # if user_id is None:
        #     return False
        self.user_session.remove()
        return True
