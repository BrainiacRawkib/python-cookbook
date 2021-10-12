from functools import wraps
from ch_10.ex_12 import when_imported


@when_imported('threading')
def warn_threads(mod):
    print('Threads? Are you for real?')


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    import threading

    # Example
    @when_imported('math')
    def add_logging(mod):
        mod.cos = logged(mod.cos)
        mod.sin = logged(mod.sin)
