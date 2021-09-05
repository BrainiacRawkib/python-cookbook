# performing complex-valued math
import math
import cmath

a = complex(2, 4)
b = 3 - 5j

print(a, b)
print(a.real, a.imag)
print(a.conjugate())
print(b.conjugate())
c = a * b
d = a / b
print(c)
print(d)

print('cmath.sin() --> ', cmath.sin(a))
print('cmath.cos() --> ', cmath.cos(a))
print('cmath.exp() --> ', cmath.exp(a))
# print(math.sqrt(-1))  # ValueError: math domain error
print(cmath.sqrt(-1))

if __name__ == '__main__':
    pass
