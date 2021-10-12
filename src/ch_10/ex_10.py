# importing modules using a name given in a string
import importlib


math = importlib.import_module('math')
mod = importlib.import_module('urllib.request')

# using import_module() to perform relative imports
# Same as 'from . import b'
b = importlib.import_module('.b', __package__)

if __name__ == '__main__':
    print(math.sin(2))
    u = mod.urlopen('https://www.python.org')
