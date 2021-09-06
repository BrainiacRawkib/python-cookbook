# iterating over multiple sequences simultaneously
from itertools import zip_longest

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):
    print(x, y)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

for i in zip(a, b):
    print(i)

print(format('zip_longest', '*^20s'))
for i in zip_longest(a, b):
    print(i)

# or
print(format('zip_longest with a fillvalue', '*^40s'))
for i in zip_longest(a, b, fillvalue=0):
    print(i)

if __name__ == '__main__':
    pass
