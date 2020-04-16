from redis import Redis
from direct_redis.functions import *


class DirectRedis(Redis):
    def keys(self, pattern: str = "*"):
        encoded = super().keys(pattern)
        return [convert_get_type(key, force_decode=False) for key in encoded]

    def hkeys(self, name):
        encoded = super().hkeys(name)
        return [convert_get_type(key, force_decode=False) for key in encoded]

    def type(self, name):
        encoded = super().type(name)
        return convert_get_type(encoded, force_decode=False)

    def set(self, key, value, ex=None, px=None, nx=False, xx=False):
        return super().set(key, convert_set_type(value))

    def hset(self, name, key, value):
        return super().hset(name, key, convert_set_type(value))

    def hmset(self, name, mapping):
        if not isinstance(mapping, dict):
            raise Exception("mapping must be a python dictionary")
        else:
            mapping = convert_set_mapping_dic(mapping)
            return super().hmset(name, mapping)

    def get(self, key, force_decode=False):
        encoded = super().get(key)
        return convert_get_type(encoded, force_decode)

    def hget(self, name, key, force_decode=False):
        encoded = super().hget(name, key)
        return convert_get_type(encoded, force_decode)

    def hmget(self, name, *keys, force_decode=False):
        encoded = super().hmget(name, *keys)
        return [convert_get_type(value, force_decode) for value in encoded]

    def hvals(self, name, force_decode=False):
        encoded = super().hvals(name)
        return [convert_get_type(value, force_decode) for value in encoded]

    def hgetall(self, name, force_decode=False):
        encoded = super().hgetall(name)
        dic = dict()
        for k, v in encoded.items():
            new_k = k.decode('utf-8')
            dic[new_k] = convert_get_type(v, force_decode)
        return dic

    def sadd(self, name, *values):
        encoded = [convert_set_type(value) for value in values]
        return super().sadd(name, *encoded)

    def smembers(self, name, force_decode=False):
        # TODO: return type set과 list 중에 고민
        encoded = super().smembers(name)
        return [convert_get_type(value, force_decode) for value in encoded]

    def lpush(self, name, *values):
        encoded = [convert_set_type(value) for value in values]
        return super().lpush(name, *encoded)

    def rpush(self, name, *values):
        encoded = [convert_set_type(value) for value in values]
        return super().rpush(name, *encoded)

    def lrange(self, name, start=0, end=-1, force_decode=False):
        """
        If start and end are not defined, returns everything.
        :param str name: key name
        :param int start: starting index. default 0: first index
        :param int end: ending index. default -1: ending index
        :param bool force_decode: forcing deserialize rather than decoding utf-8
        :return: list
        """
        encoded = super().lrange(name, start, end)
        return [convert_get_type(value, force_decode) for value in encoded]
