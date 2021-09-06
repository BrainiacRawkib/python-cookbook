# flattening a nested sequence
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    print(isinstance(items, Iterable))
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
            print('->', isinstance(x, Iterable))
        else:
            yield x

# Using yield from in the first function leads to cleaner code
# unlike the second function that adds an additional for loop


def flatten2(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield x
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8, ['str', b'bytes'], 90]

for x in flatten(items):
    print(x, end=' ')

print('\n\n', format('Working on strings too', '*^40s'))

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]

for x in flatten(items):
    print(x)

if __name__ == '__main__':
    pass
