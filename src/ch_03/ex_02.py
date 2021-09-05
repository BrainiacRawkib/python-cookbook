# performing accurate decimal calculations
import math
from decimal import Decimal, localcontext

a = Decimal('4.2')
b = Decimal('2.1')

c = a + b

print(c)
print(c == Decimal('6.3'))

# using localcontext
a = Decimal(1.3)
b = Decimal(1.6)
print(a / b)  # without localcontext

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 20
    print(a / b)

# caution
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))  # notice how 1 disappears
print(math.fsum(nums))  # prints the 1

if __name__ == '__main__':
    pass
