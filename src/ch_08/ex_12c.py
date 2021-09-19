# collections module defines a variety of ABCs
import collections

# Check if x is a sequence
x = {}
if isinstance(x, collections.Sequence):
    print('Passed!')
else:
    print('Failed!')

# Check if x is iterable
if isinstance(x, collections.Iterable):
    print('Passed!')
else:
    print('Failed!')

# Check if x has a size
if isinstance(x, collections.Sized):
    print('Passed!')
else:
    print('Failed!')

# Check if x is a mapping
if isinstance(x, collections.Mapping):
    print('Passed!')
else:
    print('Failed!')


if __name__ == '__main__':
    pass
