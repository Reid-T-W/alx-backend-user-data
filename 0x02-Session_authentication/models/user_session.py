#!/usr/bin/env python3
""" User session module
"""


class UserSession(Base):
    """ User session module
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Overriding init """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
