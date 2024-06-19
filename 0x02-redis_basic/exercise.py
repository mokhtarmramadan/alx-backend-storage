#!/usr/bin/env python3
''' Redis '''
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn:
            Callable = None) -> Union[str, bytes, int, float]:
        ''' take a key string argument and an optional Callable argument
        named fn. This callable will be used to convert the data back to the
        desired format '''
        data = self._redis.get(key)
        if fn is not None:
            data = fn(key)
        return data

    def get_str(self, key: str) -> str:
        ''' calls get passing to it a key and a callable fun that
        spcefies the type as str '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        ''' calls get passing to it a key and a callable fun that
        spcefies the type as an int '''
        return self.get(key, lambda x: int(x))
