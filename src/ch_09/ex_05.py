# defining a decorator with user adjustable attributes
import logging
from functools import wraps, partial
from ch_09.ex_01 import timethis


# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


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
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        @attach_wrapper(wrapper)
        def get_level():
            return level

        @attach_wrapper(wrapper)
        def get_message():
            return message

        # Alternatively
        wrapper.get_level = lambda: level
        wrapper.get_message = lambda: logmsg

        return wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!!!')


@timethis
@logged(logging.DEBUG, None, 'time down')
def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pass
