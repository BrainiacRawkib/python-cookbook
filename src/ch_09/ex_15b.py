# To support keyword arguments in a metaclass, define them on the
# __prepare__(), __new__(), and __init__() using keyword-only arguments


class MyMeta(type):
    # Optional

    @classmethod
    def __prepare__(cls, name, bases):
        # Custom processing
        # ...
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        # ...
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        # ...
        super().__init__(name, bases, ns)


# NB: When writing metaclasses, it is somewhat common to only define a __new__()
# or __init__() method, but not both. However, if extra keyword arguments are going
# to be accepted, then both methods must be provided and given compatible signatures
# The default __prepare__() method accepts any set of keyword arguments, but
# ignores them. It is only defined if the extra arguments would somehow affect
# management of the class namespace creation.
