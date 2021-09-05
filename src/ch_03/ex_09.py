# calculating with large numerical arrays
import numpy as np

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x + 10)

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

print(format('using numpy', '*^20s'))
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)


def f(x):
    return 3 * x ** 2 - 2 * x + 7


print('f(ax) --> ', f(ax))
print('np.sqrt(ax) --> ', np.sqrt(ax))
print('np.cos(ax) --> ', np.cos(ax))

if __name__ == '__main__':
    pass
