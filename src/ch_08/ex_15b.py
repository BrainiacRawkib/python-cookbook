# if there many methods to delegate
class A:
    def spam(self, x):
        return 'A.spam()'

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def foo(self):
        # Delegate ti the self._a instance
        return self._a.foo()

    def bar(self):
        return 'B.bar()'

    # if there are many methods to write
    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        return getattr(self._a, name)


if __name__ == '__main__':
    b = B()
    print(b.bar())  # Calls B.bar() (exists on B)
    print(b.spam(34))  # Calls B.__getattr__('spam') and delegates A.spam
