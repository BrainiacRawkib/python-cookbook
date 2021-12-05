# Issuing Warning Messages
import warnings


def func(x, y, lofile=None, debug=False):
    if lofile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)
    """
    The arguments to warn() are a warning message along with a warning class, which is
    typically one of the following: UserWarning, DeprecationWarning, SyntaxWarning,
    RuntimeWarning, ResourceWarning, or FutureWarning.
    """
