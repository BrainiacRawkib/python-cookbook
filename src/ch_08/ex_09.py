# creating a new kind of class or instance attribute
# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int!!!')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Descriptors can only be defined at the class level,
# not on a per-instance basis.

# Doesn't work
class Point2:
    def __init__(self, x, y):
        self.x = Integer('x')  # No! Must be a class variable
        self.y = Integer('y')
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(2, 4)  # Calls Point.x.__get__(p, Point)
    print(p.x)
    # If a descriptor is accessed as a class variable, the instance
    # argument is set to None
    print(Point.x)  # Calls Point.x.__get__(None, Point)
    p.x = 23.4
    print(p.x)
