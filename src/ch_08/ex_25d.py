class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError('Can\'t instantiate directly!')

    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name


if __name__ == '__main__':
    import weakref

    class CachedSpamManager:
        def __init__(self):
            self._cache = weakref.WeakValueDictionary()

        def get_spam(self, name):
            if name not in self._cache:
                s = Spam._new(name)  # Modified creation
                self._cache[name] = s
            else:
                s = self._cache[name]
            return s
