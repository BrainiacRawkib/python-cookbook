# simplifying the initialization of data structures
import math
from decimal import Decimal, localcontext


class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x', 'y']


class Circle(Structure):
    _fields = ['radius']

    def area(self):
        with localcontext() as ctx:
            ctx.prec = 4
            return Decimal(math.pi) * Decimal(self.radius ** 2)


# Example class definitions
if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    p = Point(2, 3)
    c = Circle(4.5)
    print(s)
    print(p)
    print(c.area())
