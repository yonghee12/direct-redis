import struct
import pickle

__all__ = [
    "convert_set_type",
    "convert_set_mapping_dic",
    "convert_get_type"
]


def isinstances(object, classinfos: list):
    inspection = [isinstance(object, c) for c in classinfos]
    return any(inspection)


def convert_set_type(value):
    if isinstance(value, str):
        return value
    else:
        return pickle.dumps(value)


def convert_set_mapping_dic(dic):
    new_dic = {}
    for k, v in dic.items():
        new_dic[k] = convert_set_type(v)
    return new_dic


def convert_get_type(encoded, pickle_first):
    if encoded is None:
        return None
    else:
        if pickle_first:
            try:
                return pickle.loads(encoded)
            except Exception as e:
                print(e)
                try:
                    return encoded.decode("utf-8")
                except Exception as e:
                    print(e)
                    return encoded
        else:
            try:
                return encoded.decode("utf-8")
            except UnicodeDecodeError:
                try:
                    return pickle.loads(encoded)
                except Exception as e:
                    print(e)
                    return encoded


def serialize_np(np_array):
    shape = np_array.shape
    if len(shape) == 1:
        d1 = np_array.shape[0]
        d2, d3 = 0, 0
    elif len(shape) == 2:
        d1, d2 = np_array.shape
        d3 = 0
    elif len(shape) == 3:
        d1, d2, d3 = np_array.shape
    else:
        raise Exception("Redis Can Only Store 1d, 2d, and 3d Numpy Arrays")
    dtype = np_array.dtype.num
    packed_data = struct.pack('>IIII', dtype, d1, d2, d3)
    encoded = packed_data + np_array.tobytes()
    return encoded


def unserialize_np(encoded):
    dtype, d1, d2, d3 = struct.unpack('>IIII', encoded[:16])
    np_array = np.frombuffer(encoded, offset=16, dtype=np.typeDict[dtype])
    if d3 != 0:
        np_array = np_array.reshape(d1, d2, d3)
    elif d2 != 0:
        np_array = np_array.reshape(d1, d2)
    return np_array
