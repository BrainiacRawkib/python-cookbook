# making an n-argument callable work as a callable with fewer arguments
from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)
s1(2, 3, 4)
s1(4, 5, 6)

s2 = partial(spam, d=42)
s2(0, 8, 9)
# s2(0, 8, 9, 40)  # TypeError: spam() got multiple values for argument 'd'

s3 = partial(spam, 1, 4, 5)
s3('new')

if __name__ == '__main__':
    pass
