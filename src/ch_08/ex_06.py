# creating managed attributes
class Person:
    def __init__(self, first_name):
        # the value of this attr is stored in self._first_name
        # self.first_name automatically calls the setter function
        # during initialization for type checking (i.e check whether
        # the value passed is a string).
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string!')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can\'t delete attribute!')


if __name__ == '__main__':
    p = Person('Guido')
    print(p.first_name)
    print(Person.first_name.fget)
    print(Person.first_name.fset)
    print(Person.first_name.fdel)
    # p.first_name = 34
    # print(p)
    # del p.first_name
