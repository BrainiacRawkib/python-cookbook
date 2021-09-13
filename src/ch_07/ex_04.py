# returning multiple values from a function
from typing import Tuple


def func(*x: int, y: int, z: int) -> Tuple:
    return x, y, z


a, b, c = func(1, 2, 3, y=23, z=21)

print(*a, b, c)
print(func.__annotations__)

x = 0, 12, 34
print(x)

if __name__ == '__main__':
    pass
