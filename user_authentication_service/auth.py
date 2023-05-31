#!/usr/bin/env python3
""" Authentication file"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ Return a hash password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Constructor method for Auth"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        user = self._db._session.query(
            User).filter(User.email == email).first()
        if user:
            raise ValueError(f'User {email} already exists.')
        hash_password = _hash_password(password)
        new_user = self._db.add_user(email, hash_password)
        return new_user
