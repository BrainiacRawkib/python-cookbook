from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


# decorated function
print(add(2, 3))

# original function
print(add.__wrapped__(2, 3))

if __name__ == '__main__':
    pass
