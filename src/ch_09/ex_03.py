# unwrapping a decorator
from functools import wraps


def somedecorator(func):
    @wraps(func)
    def deco(*args, **kwargs):
        pass
    return deco


@somedecorator
def add(x, y):
    return x + y


orig_add = add.__wrapped__
print(orig_add(3, 7))

if __name__ == '__main__':
    pass
