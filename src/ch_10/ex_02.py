# controlling the import of everything
# define a variable __all__ in your module that explicitly lists the
# exported names.

def spam():
    pass


def grok():
    pass


blah = 42

# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']

"""
NB:
Although the use of from module import * is strongly discouraged, it still sees frequent
use in modules that define a large number of names. If you don’t do anything, this form
of import will export all names that don’t start with an underscore. On the other hand,
if __all__ is defined, then only the names explicitly listed will be exported.
If you define __all__ as an empty list, then nothing will be exported. 
An AttributeError is raised on import if __all__ contains undefined names.
"""
