#!/usr/bin/env python3
"""Importing libraries"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """cache class"""
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """get method"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str):
        """str method"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """get int method"""
        return self.get(key, fn=int)
