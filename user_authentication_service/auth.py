#!/usr/bin/env python3
""" Authentication file"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hash_password = _hash_password(password)
            user = self._db.add_user(email, hash_password)
            return user
        raise ValueError(f'User {email} already exists')