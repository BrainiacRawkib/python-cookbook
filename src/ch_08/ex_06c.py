import math
from decimal import Decimal, localcontext


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        with localcontext() as ctx:
            ctx.prec = 4
            return Decimal(math.pi) * Decimal(self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4.0)
    print(c.radius)
    print(c.area)
    print(c.perimeter)
