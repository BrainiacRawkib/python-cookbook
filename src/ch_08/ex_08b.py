# if you want to extend only one method of a parent property
from ch_08.ex_08 import Person


class SubPerson(Person):
    @property  # Doesn't work!!!  AttributeError: can't set attribute
    def name(self):
        print('Getting name')
        return super(SubPerson, self).name()


class SubPerson2(Person):
    @Person.name.getter  # It works because it explicitly defines the only property method needed and the rest are
    # copied to the SubPerson2 subclass.
    def name(self):
        print('Getting name')
        return super(SubPerson2, self).name()


# or alternatively for just setter
class SubPerson3(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to:', value)
        super(SubPerson2, SubPerson2).name.__set__(self, value)


if __name__ == '__main__':
    p = SubPerson('Guido')
    p.name = 'Python'
    p.name
