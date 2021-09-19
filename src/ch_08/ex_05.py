# encapsulating names in a class
class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1  # a public attribute

    def public_method(self):
        """A public method."""
        pass

    def _internal_method(self):
        """An internal method."""
        pass


class B:
    def __init__(self):
        """Initialize class."""
        self.__private = 0

    def __private_method(self):
        """A private method."""
        print('I am B class')

    def public_method(self):
        """A public method."""
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        print('I am C class')


help(A)

if __name__ == '__main__':
    pass
