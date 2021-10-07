# writing decorators that add arguments to wrapped functions
from functools import wraps
from inspect import signature


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    spam(1, 2, 3)
    spam(1, 2, 3, debug=True)
    print(signature(spam))  # it won't reflect the signature of the wrapper function in the decorator
    print(signature(optional_debug))
