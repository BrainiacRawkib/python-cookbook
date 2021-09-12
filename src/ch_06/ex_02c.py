# serializing instances of a class
import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# p = Point(2, 3)  # instances are not JSON serializable by default

# to serialize instances. supply a function that takes an instance as input and returns dictionary
# that can be serialized


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


# dictionary mapping names to known classes
classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d


p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
print(a)
print(a.x)
print(vars(Point(1, 2)))

if __name__ == '__main__':
    pass
