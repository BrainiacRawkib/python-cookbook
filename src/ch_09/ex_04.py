# defining a decorator that takes arguments
import logging
from functools import wraps


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    :param level:
    :param name:
    :param message:
    :return:
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__module__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example', 'Critically')
def spam():
    print('Spam!!!')  # outputs Critically


@logged(logging.CRITICAL, 'example')
def spam2():
    print('Spam!!!')  # outputs __main__

# print(add(2, 3))
spam()
print(format('Spam2', '*^10s'))
spam2()

if __name__ == '__main__':
    pass
