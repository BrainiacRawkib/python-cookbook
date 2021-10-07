# To use a metaclass, you'd generally incorporate it into a top-level
# base class from which other objects inherit.
from ch_09.ex_17 import MyMeta


class Root(metaclass=MyMeta):
    pass


class A(Root):
    pass


class B(Root):
    pass
