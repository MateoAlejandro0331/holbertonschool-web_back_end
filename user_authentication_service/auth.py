#!/usr/bin/env python3
""" Authentication file"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Return a hash password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a unique uuid"""
    new_uuid = uuid.uuid4()
    return str(new_uuid)


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

    def valid_login(self, email: str, password: str) -> bool:
        """check if there is a valid login"""
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(
                    password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except BaseException:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session id"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            if user:
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except BaseException:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """get user from session id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user.session_id is None or not user:
                return None
            return user
        except BaseException:
            return None

    def destroy_session(self, user_id: int) -> None:
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            return None
        except BaseException:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """reset the reset_token user field in the database"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                id = _generate_uuid()
                self._db.update_user(user.id, reset_token=id)
                return id
            raise ValueError
        except NoResultFound:
            raise ValueError
