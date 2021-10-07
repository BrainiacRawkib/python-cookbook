# enforcing coding conventions in classes
class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super(MyMeta, cls).__new__(cls, clsname, bases, clsdict)


# Alternatively if __init__() is defined
class MyMeta2(type):
    def __init__(self, clsname, bases, clsdict):
        super(MyMeta2, self).__init__(clsname, bases, clsdict)
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary


class A(MyMeta):
    pass


class B(A, MyMeta2):
    pass


if __name__ == '__main__':
    print(A.__bases__)
    print(B.__bases__)
    print(A.__dict__)
