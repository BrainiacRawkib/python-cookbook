"""This code doesn't quite work."""
import weakref


class Spam:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super(Spam, cls).__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


if __name__ == '__main__':
    s = Spam('Dave')
    print(s)
    t = Spam('Dave')
    print(t)
    print(s is t)
