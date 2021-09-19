class A:
    def spam(self):
        print('A.spam')
        super(A, self).spam()


class B:
    def spam(self):
        print('B.spam')


class C(A, B):
    pass


if __name__ == '__main__':
    # a = A()
    # a.spam()
    c = C()
    c.spam()
    print(C.__mro__)
