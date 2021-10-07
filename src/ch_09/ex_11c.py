# adding wrapper function args in the decorator to the wrapped function signature
import inspect
from functools import wraps


def optional_debug(func):
    if 'debug' in inspect.getfullargspec(func).args:
        raise TypeError('debug argument already defined!')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


@optional_debug
def spam(a, b, c):  # prints spam signature and wrapper signature
    print(a, b, c)


@optional_debug
def spam(a, b, c, debug=None):  # TypeError: debug argument already defined!
    print(a, b, c)


if __name__ == '__main__':
    spam(1, 2, 3)
    # spam(1, 2, 3, debug=True)
    print(inspect.signature(spam))  # it won't reflect the signature of the wrapper function in the decorator
    print(inspect.signature(optional_debug))
