# Making Your Programs Run Faster

import sys
import csv

# runs slower
with open(sys.argv[1]) as f:
    for row in csv.reader(f):
        # Some kind of processing
        pass


"""
A little-known fact is that code defined in the global scope like this runs slower than
code defined in a function. The speed difference has to do with the implementation of
local versus global variables (operations involving locals are faster). So, if you want to
make the program run faster, simply put the scripting statements in a function:
"""


# runs faster
def main(filename):
    with open(filename) as f:
        for row in csv.reader(f):
            # Some kind of processing
            pass


main(sys.argv[1])

if __name__ == '__main__':
    pass
