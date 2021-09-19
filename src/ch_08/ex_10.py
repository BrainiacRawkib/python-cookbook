# using lazily computed properties
import math
from decimal import Decimal, localcontext


# more efficient but causes computed values to become mutable after
# it's created
class LazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


# less efficient but does not cause computed values to become mutable after
# it's created.
def lazyproperty(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        with localcontext() as ctx:
            ctx.prec = 4
            return Decimal(math.pi) * Decimal(self.radius ** 2)

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        with localcontext() as ctx:
            ctx.prec = 4
            return 2 * Decimal(math.pi) * Decimal(self.radius)


if __name__ == '__main__':
    c = Circle(4.0)
    print(c.radius)
    print(c.area)
    print(c.perimeter)
    print(vars(c))
