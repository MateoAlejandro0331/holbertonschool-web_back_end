#!/usr/bin/env python3
"""Create a class auth"""
from typing import List, TypeVar
from flask import request


class Auth():
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication"""
        if path is None:
            return True
        if len(excluded_paths) == 1 and "/api/v1/status/" in excluded_paths \
                and path == "/api/v1/status":
            return False
        if path not in excluded_paths:
            return True
        if not excluded_paths or excluded_paths is None:
            return True
 
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
