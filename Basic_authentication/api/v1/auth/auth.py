#!/usr/bin/env python3
"""Create a class auth"""
from typing import List, TypeVar


class Auth():
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication"""
        if path is None:
            return True
        if not excluded_paths or excluded_paths is None:
            return True
        if excluded_paths and "/api/v1/status/" in excluded_paths \
                and path == "/api/v1/status":
            return False
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is None:
            return None
        if request.headers.get("Authorization") is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
