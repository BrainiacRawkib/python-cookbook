# Defining classes programmatically
# stack.py
# Example of making a class manually from parts
"""You can use the types.new_class() to instantiate new class objects.
All you need to do is provide the NAME of the class, the TUPLE of PARENT CLASS,
KEYWORD ARGUMENTS, and a CALLBACK that populates the class dictionary with members."""


# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}


if __name__ == '__main__':
    # Make a class
    import abc
    import types

    Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
    Stock.__module__ = __name__

    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s.cost())
    print(Stock.__module__)

    # If the class you want to create involves a different metaclass
    # it would be specified in the third argument to types.new_class()
    Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta},
                            lambda ns: ns.update(cls_dict))
    Stock.__module__ = __name__
    print(Stock)
    print(type(Stock))
