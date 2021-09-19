# delegation can also be used as an alternative to inheritance
class A:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')


class S:
    pass


class B(A, S):
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print('B.spam', x)
        self._a.spam(x)

    def bar(self):
        print('B.bar')

    def __getattr__(self, name):
        return getattr(self._a, name)


if __name__ == '__main__':
    b = B()
    b.spam('spam')
    print(B.__bases__)  # prints out the parent classes in the order of occurrence
