# extending classes with mixins
class LoggedMappingMixin:
    """
    Add logging to get/set/delete operations for debugging.
    """
    __slots__ = ()  # the specification __slots__ = () is meant to serve as a strong hint
    # that the mixin classes do not have their own instance data.

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super(LoggedMappingMixin, self).__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ', str(key))
        return super(LoggedMappingMixin, self).__delitem__(key)


class SetOnceMappingMixin:
    """
    Only allow a key to be set once.
    """
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super(SetOnceMappingMixin, self).__setitem__(key, value)


class StringKeysMappingMixin:
    """
    Restrict keys to strings only.
    """
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('Keys must be strings')
        return super(StringKeysMappingMixin, self).__setitem__(key, value)
