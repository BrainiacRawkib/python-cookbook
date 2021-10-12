# creating a new module object
import imp
import sys

# m = imp.new_module('spam')

# combining caching and module creation in a single step
m = sys.modules.setdefault('spam', imp.new_module('spam'))


if __name__ == '__main__':
    print(m)
    print(m.__name__)
    print(m.__file__)
    print(m.__package__)
