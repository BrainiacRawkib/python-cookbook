# this recipe is also severely limited in its support for inheritance
from ch_09.ex_20b import *


class A:
    pass


class B(A):
    pass


class C:
    pass


class Spam(metaclass=MultipleMeta):
    def foo(self, x: A):
        print('Foo 1:', x)

    def foo(self, x: C):
        print('Foo 2:', x)


if __name__ == '__main__':
    s = Spam()
    a = A()
    s.foo(a)
    b = B()
    s.foo(b)
