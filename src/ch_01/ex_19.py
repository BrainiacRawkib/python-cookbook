# transforming and reducing data at the same time
import os

nums = [1, 2, 3, 4, 5]

s = sum(x * x for x in nums)

# determine if any .py file exists in a directory
path = './'  # or use os.getcwd()
files = os.listdir(path)
if any(name.endswith('.py') for name in files):
    print('There be python!', files)
else:
    print('Sorry, no python!')

# output a tuple as CSV
x = ('ACME', 50, 1234.543)

# data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
min_shares2 = min(portfolio, key=lambda s: s['shares'])

if __name__ == '__main__':
    print(s)
    print(os.listdir())
    print(','.join(str(i) for i in x))
    print(min_shares)
    print(min_shares2)
