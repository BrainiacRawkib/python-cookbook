# formatting numbers for output
x = 1234567.56789

# two decimal places of accuracy
print(format(x, '0.2f'))

# right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))

# left justified in 10 chars, one-digit accuracy
print(format(x, '<10.1f'))

# centered
print(format(x, '^10.1f'))

# inclusion of thousands separator
print(format(x, ','))
print(format(x, '0,.1f'))

# formatted as round() method
print('formatted as round -->', format(-x, '0,.2f'), '\n')

# exponential notation
print(format('exponential notation', '*^30s'))
print(format(x, 'e'))
print(format(x, '.3e'))
print(format(x, '0.2E'))

a = 'The value is {:,.2f}'.format(x)
print('a ---> ', a)
a = 'The value is {:0,.2f}'.format(x)
print('a ---> ', a)

print(format('swap operators', '*^30s'))
swap_separators = {ord('.'): ',', ord(','): '.'}
print(format(x, ',').translate(swap_separators))

if __name__ == '__main__':
    pass
