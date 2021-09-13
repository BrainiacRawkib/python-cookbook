# capturing variables in anonymous functions

print(format('At runtime', '*^30s'))
x = 10
a = lambda y: x + y
# the value x = 20 is used for both a(10) and b(10) at runtime instead
# of x = 10 and x = 20 for both a and b respectively.
x = 20
b = lambda y: x + y
print(a(10))
print(b(10))

# if you want the anonymous function to capture a value at
# the point of definition and keep it, include it as a
# default value.
print(format('At point of definition', '*^30s'))
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))


if __name__ == '__main__':
    pass
