# to work around the problem of hardcoded directories if you carefully
# construct an appropriate path using module-level variables such as __file__
import sys
from os.path import abspath, join, dirname

sys.path.insert(0, abspath(dirname('__file__'), 'src'))
