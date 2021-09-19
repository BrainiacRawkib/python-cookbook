class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        # Base.__init__(self)
        super(A, self).__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        # Base.__init__(self)
        super(B, self).__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        # A.__init__(self)
        # B.__init__(self)
        super(C, self).__init__()
        print('C.__init__')


if __name__ == '__main__':
    c = C()
    c
    print(C.__mro__)
