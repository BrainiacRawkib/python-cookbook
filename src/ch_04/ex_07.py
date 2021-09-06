# taking a slice of an iterator
from itertools import islice


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# print(c[10:20])  # TypeError: 'generator' object is not subscriptable

# now using islice()
for x in islice(c, 10, 20):
    print(x)

if __name__ == '__main__':
    pass
