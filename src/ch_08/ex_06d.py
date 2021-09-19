"""
A very BAD CODING PRACTICE is to repeat property method
for different attributes.
See ch_08.ex_8.9 and ch_09.ex_9.21 for better examples.
"""


class Person:
    """Bad coding practice."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string!')
        self._first_name = value

    @ first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute!")

    # Repeated property code, but for a different attribute (bad!)
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string!')
        self._last_name = value


if __name__ == '__main__':
    print(Person.__dict__)
