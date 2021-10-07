# initializing class members at definition time
# check http://www.python.org/dev/peps/pep-0422 for alternative recipe
import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super(StructTupleMeta, cls).__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super(StructTuple, cls).__new__(cls, args)


# this allow simple tuple-based data structure to be defined.
class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']


if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s)
    # s.shares = 45  # AttributeError: can't set attribute
    # s = Stock(('ACME', 50, 91.1))  # ValueError: 3 arguments required
