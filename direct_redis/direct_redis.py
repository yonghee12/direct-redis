from redis import Redis
from direct_redis.functions import *


class DirectRedis(Redis):
    def keys(self, pattern: str = "*"):
        encoded = super().keys(pattern)
        return [convert_get_type(key, pickle_first=False) for key in encoded]

    def randomkey(self, pickle_first=False):
        encoded = super().randomkey()
        return convert_get_type(encoded, pickle_first)

    def type(self, name):
        encoded = super().type(name)
        return convert_get_type(encoded, pickle_first=False)

    def set(self, key, value, ex=None, px=None, nx=False, xx=False):
        return super().set(key, convert_set_type(value))

    def get(self, key, pickle_first=False):
        encoded = super().get(key)
        return convert_get_type(encoded, pickle_first)

    def mset(self, mapping):
        if not isinstance(mapping, dict):
            raise Exception("mapping must be a python dictionary")
        else:
            mapping = convert_set_mapping_dic(mapping)
            return super().mset(mapping)

    def mget(self, *args, pickle_first=False):
        encoded = super().mget(args)
        return [convert_get_type(value, pickle_first) for value in encoded]

    def hkeys(self, name):
        encoded = super().hkeys(name)
        return [convert_get_type(key, pickle_first=False) for key in encoded]

    def hset(self, name, key, value):
        return super().hset(name, key, convert_set_type(value))

    def hmset(self, name, mapping):
        if not isinstance(mapping, dict):
            raise Exception("mapping must be a python dictionary")
        else:
            mapping = convert_set_mapping_dic(mapping)
            return super().hmset(name, mapping)

    def hget(self, name, key, pickle_first=False):
        encoded = super().hget(name, key)
        return convert_get_type(encoded, pickle_first)

    def hmget(self, name, *keys, pickle_first=False):
        encoded = super().hmget(name, *keys)
        return [convert_get_type(value, pickle_first) for value in encoded]

    def hvals(self, name, pickle_first=False):
        encoded = super().hvals(name)
        return [convert_get_type(value, pickle_first) for value in encoded]

    def hgetall(self, name, pickle_first=False):
        encoded = super().hgetall(name)
        dic = dict()
        for k, v in encoded.items():
            new_k = k.decode('utf-8')
            dic[new_k] = convert_get_type(v, pickle_first)
        return dic

    def sadd(self, name, *values):
        encoded = [convert_set_type(value) for value in values]
        return super().sadd(name, *encoded)

    def srem(self, name, *values):
        encoded = [convert_set_type(value) for value in values]
        return super().srem(name, *encoded)

    def sismember(self, name, value):
        encoded = convert_set_type(value)
        return super().sismember(name, encoded)

    def smembers(self, name, pickle_first=False):
        encoded = super().smembers(name)
        return {convert_get_type(value, pickle_first) for value in encoded}

    def spop(self, name, pickle_first=False):
        encoded = super().spop(name)
        return convert_get_type(encoded, pickle_first)

    def srandmember(self, name, count=None, pickle_first=False):
        encoded = super().srandmember(name, number=count)
        if isinstance(encoded, list):
            return [convert_get_type(value, pickle_first) for value in encoded]
        else:
            return convert_get_type(encoded, pickle_first)

    def sdiff(self, primary_set, *comparing_sets):
        encoded = super().sdiff(primary_set, *comparing_sets)
        return {convert_get_type(value, pickle_first=False) for value in encoded}

    def lpush(self, name, *values):
        encoded = [convert_set_type(value) for value in values]
        return super().lpush(name, *encoded)

    def lpushx(self, name, value):
        return super().lpushx(name, convert_set_type(value))

    def rpushx(self, name, value):
        return super().rpushx(name, convert_set_type(value))

    def rpush(self, name, *values):
        encoded = [convert_set_type(value) for value in values]
        return super().rpush(name, *encoded)

    def lpop(self, name, pickle_first=False):
        encoded = super().lpop(name)
        return convert_get_type(encoded, pickle_first)

    def rpop(self, name, pickle_first=False):
        encoded = super().rpop(name)
        return convert_get_type(encoded, pickle_first)

    def lindex(self, name, index, pickle_first=False):
        encoded = super().lindex(name, index)
        return convert_get_type(encoded, pickle_first)

    def lrange(self, name, start=0, end=-1, pickle_first=False):
        """
        If start and end are not defined, returns everything.
        :param str name: key name
        :param int start: starting index. default 0: first index
        :param int end: ending index. default -1: ending index
        :param bool pickle_first: forcing deserialize rather than decoding utf-8
        :return: list
        """
        encoded = super().lrange(name, start, end)
        return [convert_get_type(value, pickle_first) for value in encoded]
