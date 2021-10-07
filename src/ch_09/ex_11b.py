# avoiding name clash between decorator and wrapped function
import inspect
from functools import wraps


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined!')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def spam(a, b, c, debug=None):  # TypeError: debug argument already defined!
    print(a, b, c)


if __name__ == '__main__':
    spam(1, 2, 3)
    # spam(1, 2, 3, debug=True)
    print(inspect.signature(spam))  # it won't reflect the signature of the wrapper function in the decorator
    print(inspect.signature(optional_debug))

