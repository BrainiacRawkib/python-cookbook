class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):

    def foo_bar(self):  # ok
        pass


class B(Root):

    def fooBar(self):  # raises TypeError
        pass


if __name__ == '__main__':
    print(A())
