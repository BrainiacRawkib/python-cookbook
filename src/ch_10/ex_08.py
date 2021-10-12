# reading datafiles within a package

"""
mypackage/
    __init__.py
    somedata.dat
    spam.py
"""

"""
Now suppose the file spam.py wants to read the contents of the file somedata.dat.
To do it, use the following code:
"""

import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
