# defining anonymous or inline functions
add = lambda x, y: x + y

print(add(34, 45))
print(add('Hello ', 'World!'))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
x = sorted(names, key=lambda name: name.split()[-1].lower())
print(x)

if __name__ == '__main__':
    pass
