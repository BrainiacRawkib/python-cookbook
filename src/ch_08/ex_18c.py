class RestrictKeysMixin:
    def __init__(self, *args, _restrict_key_type, **kwargs):
        self.__restrict_key_type = _restrict_key_type
        super(RestrictKeysMixin, self).__init__(*args, **kwargs)  # use of super() is very essential and
        # critical in writing mixins classes. However, they need to call original
        # implementation of these methods.

    def __setitem__(self, key, value):
        if not isinstance(key, self.__restrict_key_type):
            raise TypeError('Keys must be ' + str(self.__restrict_key_type))
        super(RestrictKeysMixin, self).__setitem__(key, value)


# Use sample
class RDict(RestrictKeysMixin, dict):
    pass


if __name__ == '__main__':
    d = RDict(_restrict_key_type=str)
    e = RDict([('name', 'Dave'), ('n', 37)], _restrict_key_type=str)
    f = RDict(name='Dave', n=37, _restrict_key_type=str)
    print(f)
    f[3] = 10  # TypeError: Keys must be <class 'str'>
    print(f)
