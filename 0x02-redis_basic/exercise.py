#!/usr/bin/env python3
''' Redis '''
import redis
import uuid
from typing import Union


class Cache:
    ''' Cache class '''
    def __init__(self):
        ''' initialization method for cache class '''
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        ''' generate a random key (e.g. using uuid),
        store the input data in Redis '''
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
