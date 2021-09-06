# iterating on items in separate containers
from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

# more efficient
for x in chain(a, b):
    print(x)

# inefficient
for x in a + b:
    print(x)

# various working sets of items
active_items = set()
inactive_items = set()

# Iterate over all items
for item in chain(active_items, inactive_items):
    # process item
    print(item)

if __name__ == '__main__':
    pass
