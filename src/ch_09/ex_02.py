# preserving function metadata when writing decorators
import time
from functools import wraps
from inspect import signature


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
def countdown(n: int):
    """Count down."""
    while n > 0:
        n -= 1


countdown(100000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
print(signature(countdown))

if __name__ == '__main__':
    pass
