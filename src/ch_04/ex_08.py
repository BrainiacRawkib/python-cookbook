# skipping the first part of an iterable
from itertools import dropwhile, islice

with open('passwd.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')


# if the exact number of items to be skipped is known, use itertools.islice()
items = ['a', 'b', 'c', 1, 4, 10, 15]

# the last None argument to islice() is required to indicate that you
# want everything beyond the first three items as opposed to only the first three items

for x in islice(items, 3, None):
    print(x)

print(format('Another method', '*^25s'))
with open('passwd.txt') as f:
    lines = (line for line in f if not line.startswith('#'))

    for line in lines:
        print(line, end='')

if __name__ == '__main__':
    pass
