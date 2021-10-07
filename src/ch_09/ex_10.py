# applying decorators to class and static methods
import time
from functools import wraps


# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r
    return wrapper


# Class illustrating application of the decorator to different kinds of methods
class Spam:

    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


if __name__ == '__main__':
    s = Spam()
    print(format('Instance method', '*^30s'))
    s.instance_method(1000000)

    print(format('Class method', '*^30s'))
    Spam.class_method(1000000)

    print(format('Static method', '*^30s'))
    Spam.static_method(1000000)
