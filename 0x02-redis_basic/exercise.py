#!/usr/bin/env python3
''' Redis '''
import redis
import uuid
from typing import Union


class Cache:
    ''' Cache class '''
    def __init__(self) -> None:
        ''' initialization method for cache class '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' generate a random key (e.g. using uuid),
        store the input data in Redis '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
