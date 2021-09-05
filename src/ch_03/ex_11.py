# picking things at random
import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.sample(values, 2))
print(random.sample(values, 3))
random.shuffle(values)
print(values)

# producing random integers
print(format('producing random integers', '*^40s'))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))

print(format('producing uniform floating-point values', '*^50s'))
print(random.random())
print(random.random())
print(random.random())

print(format('producing random-bits expressed as int', '*^50s'))
print(random.getrandbits(20))

"""
---DISCLAIMER()---
FUNCTIONS IN random() module should not
be used in PROGRAMS RELATED TO CRYPTOGRAPHY.
Use ssl module instead; ssl.RAND_bytes() can be used 
to generate a cryptographically secure sequence.
"""

if __name__ == '__main__':
    pass
