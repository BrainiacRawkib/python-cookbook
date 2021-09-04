# combining and concatenating strings
parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print(' '.join(parts))
print('-'.join(parts))

a = 'Hello'  'World'
print(a)

data = ['ACME', 50, 91.1]
print(', '.join(str(d) for d in data))
b = 'Welcome Home'
print(a, b, sep=':')
print(a, b, end=':')

if __name__ == '__main__':
    pass
