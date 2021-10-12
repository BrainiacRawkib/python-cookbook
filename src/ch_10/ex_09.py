# adding directories to sys.path
"""
There are two common ways to get new directories added to sys.path. First, you can
add them through the use of the PYTHONPATH environment variable. For example:
"""

# bash % env PYTHONPATH=/some/dir:/other/dir python3

"""
The second approach is to create a .pth file that lists the directories like this:

# myapplication.pth
/some/dir
/other/dir
"""

# to write code that manually adjusts the value of sys.path
import sys
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')

"""
Although this “works,” it is extremely fragile in practice and should be avoided if possible.
Part of the problem with this approach is that it adds hardcoded directory names
to your source. This can cause maintenance problems if your code ever gets moved
around to a new location. It’s usually much better to configure the path elsewhere in a
manner that can be adjusted without making source code edits.
"""
