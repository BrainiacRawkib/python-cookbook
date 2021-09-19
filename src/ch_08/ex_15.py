# delegating attribute access
class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internet self._a instance
        return self._a

    def foo(self):
        # Delegate ti the self._a instance
        return self._a.foo()

    def bar(self):
        pass


if __name__ == '__main__':
    b = B()
    print(b.bar())
    print(b.spam(34))
