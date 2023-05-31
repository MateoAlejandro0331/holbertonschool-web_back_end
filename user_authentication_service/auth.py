#!/usr/bin/env python3
""" Authentication file"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Return a hash password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
