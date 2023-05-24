#!/usr/bin/env python3
"""Create a class BasicAuth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication"""

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """Methos to check authorization"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        strings = authorization_header.split()
        if strings[0] != 'Basic':
            return None
        return strings[1]
