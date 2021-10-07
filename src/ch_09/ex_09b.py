from functools import wraps


def profiled(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper


# Example
@profiled
def add(x, y):
    return x + y


if __name__ == '__main__':
    add(2, 3)
    add(29, 30)
    print(callable(add.ncalls))
    print(add.ncalls())
    print(add.ncalls)
