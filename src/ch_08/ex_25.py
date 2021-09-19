# creating cached instances
import logging


# The class in question
class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
# d = get_spam('bar')

print(a is b)
print(a is c)
# print(b is d)

print(list(_spam_cache))
del a
del c
del b
print(list(_spam_cache))

if __name__ == '__main__':
    print(format('Entering logging module', '*^40s'))
    a = logging.getLogger('foo')
    b = logging.getLogger('bar')
    c = logging.getLogger('foo')
    d = logging.getLogger('bar')

    print(a is b)
    print(a is c)
    print(b is d)
