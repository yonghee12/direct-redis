from redis import Redis
from direct_redis.functions import *


class DirectRedis(Redis):
    def set(self, key, value):
        super().set(key, convert_set_type(value))

    def hset(self, name, key, value):
        super().hset(name, key, convert_set_type(value))

    def hmset(self, name, mapping):
        if not isinstance(mapping, dict):
            raise Exception("mapping must be a python dictionary")
        else:
            mapping = convert_set_mapping_dic(mapping)
            super().hmset(name, mapping)

    def get(self, key, force_decode=False):
        encoded = super().get(key)
        return convert_get_type(encoded, force_decode)

    def hget(self, name, key, force_decode=False):
        encoded = super().hget(name, key)
        return convert_get_type(encoded, force_decode)

    def hmget(self, name, *keys, force_decode=False):
        encoded = super().hmget(name, *keys)
        return [convert_get_type(elem, force_decode) for elem in encoded]

    def hgetall(self, name, force_decode=False):
        encoded = super().hgetall(name)
        dic = dict()
        for k, v in encoded.items():
            new_k = k.decode('utf-8')
            dic[new_k] = convert_get_type(v, force_decode)
        return dic
