# from ch_09.ex_14 import *
from collections import OrderedDict


class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super(NoDupOrderedDict, self).__init__()

    def __setitem__(self, name, value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name, self.clsname))
        super(NoDupOrderedDict, self).__setitem__(name, value)


class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return NoDupOrderedDict


if __name__ == '__main__':
    class A(metaclass=OrderedMeta):
        def spam(self):
            pass

        def spam(self):
            pass
