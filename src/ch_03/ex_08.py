# calculating with fractions
from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)

print(a)
print(b)
print(a + b)

# Getting numerator/denominator
c = a * b
print(c)
print(c.numerator)
print(c.denominator)
print(float(c))

# limiting the denominator of a value
print(c.limit_denominator(8))
d = Fraction(8, 16)
print(d.limit_denominator(4))

# converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)

if __name__ == '__main__':
    pass
