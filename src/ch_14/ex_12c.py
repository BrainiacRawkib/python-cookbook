"""
If your code is deeply buried in an environment where it is difficult to obtain an interactive
shell (e.g., in a server), you can often catch errors and produce tracebacks yourself
"""
import pdb
import traceback
import sys


def sample(n):
    if n > 0:
        sample(n - 1)
    else:
        traceback.print_stack(file=sys.stderr)


"""
Alternatively, you can also manually launch the debugger at any point in your program
using pdb.set_trace() like this:
"""


def func(arg):
    pdb.set_trace()


if __name__ == '__main__':
    sample(5)
