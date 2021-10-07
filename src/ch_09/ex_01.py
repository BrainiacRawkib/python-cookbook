# putting a wrapper around a function
import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def countdown(n):
    """Count down"""
    while n > 0:
        n -= 1


countdown(100000)


class A:
    @classmethod
    def method(cls):
        pass


# or
class B:
    # Equivalent definition of a class method
    def method(cls):
        pass

    method = classmethod(method)


if __name__ == '__main__':
    pass
