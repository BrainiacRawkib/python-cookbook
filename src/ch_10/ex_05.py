# making separate directories of code import under a common namespace
"""
ex_05_foo_package/foo-package/
    spam/
        blah.py
ex_05_foo_package/bar-package/
    spam/
        grok.py
"""

"""
To unify separate directories under a common namespace, you organize the code just
like a normal Python package, but you omit __init__.py files in the directories where
the components are going to join together
"""