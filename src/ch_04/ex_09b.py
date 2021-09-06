# combinations
from itertools import combinations, combinations_with_replacement

items = ['a', 'b', 'c']

# 3 combinations
print(format('3 combinations', '*^20s'))
for c in combinations(items, 3):
    print(c)

# 2 combinations
print(format('2 combinations', '*^20s'))
for c in combinations(items, 2):
    print(c)

# 1 combinations
print(format('1 combinations', '*^20s'))
for c in combinations(items, 1):
    print(c)

# combination with replacement
print(format('1 combinations', '*^20s'))
for c in combinations_with_replacement(items, 3):
    print(c)

if __name__ == '__main__':
    pass
