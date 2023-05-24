#!/usr/bin/env python3
"""Create a class BasicAuth"""
from api.v1.auth.auth import Auth
from typing import Tuple
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """methos to decode base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """extract_user_credentials"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        data = decoded_base64_authorization_header.split(':')
        return (data[0], data[1])
