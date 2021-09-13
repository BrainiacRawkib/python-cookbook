x = 53


def spam(a, b=x):
    print(a, b)


# bad practice
def spam2(a, b=[]):
    pass


# bad practice
def spam3(a, b=None):
    if not b:  # do not use 'if not b' use 'b is None' instead
        b = []
        print(b)
    print(b)


# good practice but can't test if a user supplied an input value
def spam4(a, b=None):
    if b is None:
        b = []


_no_value = object()


# best practice and can detect if a user supplied an input value
def spam5(a, b=_no_value):
    if b is _no_value:
        print('No value supplied')
    else:
        print('Value supplied')


spam(24)
x = spam3(1, 0)
# x = spam2(2)
# print(x.append(78))
spam5(78)
spam5(23, None)

if __name__ == '__main__':
    pass
