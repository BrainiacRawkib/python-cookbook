# metaclass that checks the definition of redefined methods to make sure
# they have the same calling signature as the original method in the superclass
import logging
from inspect import signature


class MatchSignaturesMeta(type):
    """
    When working with metaclass, it's important to know that self is actually
    a class object.
    """
    def __init__(self, clsname, bases, clsdict):
        super(MatchSignaturesMeta, self).__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # Get the previous definition (if any) and compare the signatures
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, prev_sig, val_sig)


# Example
class Root(metaclass=MatchSignaturesMeta):
    pass


class A(Root):

    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass

    def __len__(self):
        pass


# Class with redefined methods, but slightly different signatures
class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass


if __name__ == '__main__':
    print(callable(A.foo))
    print(callable(A.__len__))
