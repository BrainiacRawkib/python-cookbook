# enforcing an argument signature on *args and **kwargs
from inspect import Signature, Parameter


# Make a signature for a func(x, y=42, *, z=None, **a)
parms = [
    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter('z', Parameter.KEYWORD_ONLY, default=None),
    Parameter('a', Parameter.VAR_KEYWORD)
]

sig = Signature(parms)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


if __name__ == '__main__':
    print(sig)

    # Try various examples
    func(1, 2, z=3)
    print()
    func(1)
    print()
    func(x=2, y=23)
    print()
    # func(1, 2, 3, 4)
    func(y=2)
    # func(1, y=2, x=3)
