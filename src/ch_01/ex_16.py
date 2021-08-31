# filtering sequence elements
import math
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
pos = (n for n in mylist if n > 0)
neg = (n for n in mylist if n < 0)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


int_val = list(filter(is_int, values))

sqrt = [math.sqrt(i) for i in mylist if i > 0]

clip_neg = [n if n > 0 else 0 for n in mylist]
clip_pos = [n if n < 0 else 0 for n in mylist]

# itertools.compress()
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
# more5 = [n if n > 5 else False for n in counts] alternatively

compression = list(compress(addresses, more5))

if __name__ == '__main__':
    print([n for n in mylist if n > 0])
    print([n for n in mylist if n < 0])
    for x in pos:
        print(x, end=' ')
    print()
    for x in neg:
        print(x, end=' ')
    print()
    print(int_val)
    print(sqrt)
    print(clip_neg)
    print(clip_pos)
    print(more5)
    print(compression)
