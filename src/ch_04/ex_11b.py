headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

s = dict(zip(headers, values))

for name, val in s.items():
    print(name, ' = ', val)

# or
for name, val in zip(headers, values):
    print(name, ' = ', val)

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']

for i in zip(a, b, c):
    print(i)

if __name__ == '__main__':
    pass
