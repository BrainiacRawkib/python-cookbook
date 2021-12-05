"""
If your code is deeply buried in an environment where it is difficult to obtain an interactive
shell (e.g., in a server), you can often catch errors and produce tracebacks yourself
"""
import traceback
import sys


def func(*arg):
    pass


try:
    func()
except:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)
