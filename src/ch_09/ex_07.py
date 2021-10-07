# enforcing type checking on a function using a decorator
from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


if __name__ == '__main__':
    @typeassert(int, z=int)
    def spam(x, y, z=42):
        print(x, y, z)

    spam(1, 2, 3)
    spam(1, 'hello', 34)
    # spam(1, 'hello', 'world')
    print(format('Signature', '*^20'))
    sig = signature(spam)
    print(sig)
    print(sig.parameters)
    print(sig.parameters['x'].kind)
    print(sig.parameters['z'].default)
    bound_values = sig.bind(1, 2, 3)
    print(bound_values.args)
    print(bound_values.arguments)
    print(bar(2, [1, 3, 4, 5]))
    # bar(2, 3)
    # bar(2, 3)  # TypeError: Argument items must be <class 'list'>
