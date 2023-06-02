#!/usr/bin/env python3
"""Importing libraries"""
import redis
import uuid
from functools import wraps
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """Count the number of calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call history function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))
        return output
    return wrapper


def replay(method):
    """replay function"""
    redis_client = redis.Redis()
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"
    inputs = redis_client.lrange(inputs_key, 0, -1)
    outputs = redis_client.lrange(outputs_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode()}) -> {out.decode()}")


class Cache:
    """cache class"""
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
