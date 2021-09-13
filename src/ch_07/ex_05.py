# defining functions with default arguments
def spam(a, b=34):
    """defining functions with default args."""
    print(a, b)


# using a list, set, dict as a default value
def default_spam(a, b=None):
    """
    If the default value is supposed to be a mutable container, such as
    list, set, or dictionary.
    :param a:
    :param b:
    :return:
    """
    if b is None:
        b = [] or {}


_no_value = object()


# testing whether an optional argument was given.
def test_spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied!')
    print('b-->', b)


spam(12)
spam(43, 56)
help(spam)
test_spam(12)
test_spam(34, 56)
test_spam(34, None)

if __name__ == '__main__':
    pass
