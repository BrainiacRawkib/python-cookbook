# metaclass to apply constraints
# A metaclass that applies checking
from ch_08.ex_13b import *


class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute nams ti the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


# Example
class Stock(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# metaclass simplifies code when using descriptors
# for example
# Normal without Metaclass
class Point:
    x = Integer('x')
    y = Integer('y')


# Metaclass
class Point2(metaclass=checkedmeta):
    x = Integer()
    y = Integer()
