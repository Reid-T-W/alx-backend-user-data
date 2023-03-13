#!/usr/bin/env python3
""" Authentication Module """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hash and return a password """
    binary_pw = password.encode('utf-8')
    hashed_pw = bcrypt.hashpw(binary_pw, bcrypt.gensalt())
    return hashed_pw
