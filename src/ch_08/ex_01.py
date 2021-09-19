# changing the string representation of instances
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # used as fallback if __str__ is not defined
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)


if __name__ == '__main__':
    p = Pair(3, 4)
    print(repr(p))
    print(p)
    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))  # !s is the default formatting
