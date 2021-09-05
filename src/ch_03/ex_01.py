# rounding numerical values

# rounding numbers
print(format('rounding numbers', '*^30'), end='\n\n')
print(round(123.4245, 2))
print(round(123.4245, 1))
print(round(-123.4245, 2))
print(round(123.4245))
print(round(123.4245, -1))
print(round(123.4245, -2))
print(round(123.4245, -3))
print(round(1234245, -3))

# formatting numbers
print(format('formatting numbers', '*^30'), end='\n\n')
x = 134.23489
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))
print('value is {:0.2f}'.format(x))

# avoid this practice for floating-point number and use decimal module
a = 2.1
b = 4.2
c = a + b
print(format('Avoid round() method for floating-point number', '*^70s'))
print(c)
print(c == 6.3)
print('round(c) -->', round(c + 23.456, 2))

if __name__ == '__main__':
    pass
