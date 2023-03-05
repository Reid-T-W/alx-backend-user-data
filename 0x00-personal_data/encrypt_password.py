#!/usr/bin/env python3
""" Module that hashs a password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash a password using a randomly generated salt """
    return(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ validate password """
    return(bcrypt.checkpw(password.encode('utf-8'), hashed_password))
