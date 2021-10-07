# To use the classes defined in ex_20b
import time
from ch_09.ex_20b import *


class Spam(metaclass=MultipleMeta):
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


class Spam2:
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


# Example: overloaded __init__
class Date(metaclass=MultipleMeta):
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)


if __name__ == '__main__':
    s = Spam()
    s.bar(2, 3)
    s.bar('hello')
    s.bar('hello', 5)
    # s.bar(2, 'hello')  # TypeError: No matching method for types (<class 'int'>, <class 'str'>)

    # Overloaded __init__
    e = Date(2021, 10, 2)

    # Get today's date
    print(e.year, e.month, e.day)
    print(Spam2.bar.__annotations__)

    b = s.bar
    print(b)
    print(b.__self__)
    print(b.__func__)
