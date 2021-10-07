import sys
import operator
import types
from collections import namedtuple


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


# namedtuple() uses exec() instead of the technique shown here

def named_tuple(classname, fieldnames):
    # Populate a dictionary of field property accessors
    cls_dict = {name: property(operator.itemgetter(n))
                for n, name in enumerate(fieldnames)}

    # Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    # Make the class
    cls = types.new_class(classname, (tuple,), {}, lambda ns: ns.update(cls_dict))

    # Set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


if __name__ == '__main__':
    print(Stock)
    Point = named_tuple('Point', ['x', 'y'])
    print({Point})
    p = Point(4, 5)
    print(len(p))
    p.x = 3
