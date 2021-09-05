# working with infinity and NaNs
import math

a = float('inf')  # positive infinity or inf
b = float('-inf')  # negative infinity or neg-inf
c = float('nan')  # Not a number or nan

print(a)
print(b)
print(c)

# testing the presence of inf, neg-inf and nan
print(math.isinf(a))
print(math.isnan(c))

# infinite values will propagate in calculations
print(a + 45)
print(a * 10)
print(10 / a)
print(a / a)

if __name__ == '__main__':
    pass
