# iterating over all possible combinations or permutations
# permutations
from itertools import permutations

items = ['a', 'b', 'c']

for p in permutations(items):
    print(p)

# permutations of smaller length
print(format('permutations of smaller length', '*^40s'))
for p in permutations(items, 2):
    print(p)

if __name__ == '__main__':
    pass
